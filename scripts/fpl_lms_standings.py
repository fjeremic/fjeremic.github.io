import argparse
import hashlib
import logging
from pathlib import Path

import requests
import yaml


HALVES = {'h1': (1, 19), 'h2': (20, 38)}


def fetch_json(session, url, description):
    response = session.get(url, timeout=30)

    try:
        payload = response.json()
    except ValueError as exc:
        raise RuntimeError(f"Could not decode {description} response for {url}: {response.text[:500]}") from exc

    if response.status_code != 200:
        detail = payload.get("detail") if isinstance(payload, dict) else payload
        raise RuntimeError(f"FPL {description} request failed for {url} (HTTP {response.status_code}): {detail}")

    return payload


def get_players(session, league_id):
    url = f"https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/"
    players = []
    page = 1
    while True:
        data = fetch_json(session, f"{url}?page_standings={page}", f"standings page {page}")["standings"]
        players.extend({'entry': player['entry'], 'team': player['entry_name'], 'manager': player['player_name']}
                       for player in data['results'])
        if not data['has_next']:
            break
        page += 1

    if not players:
        raise RuntimeError("LMS league has no players")
    return players


def get_standings(session, league_id, previous):
    bootstrap = fetch_json(session, "https://fantasy.premierleague.com/api/bootstrap-static/", "bootstrap")
    finalized = {event['id'] for event in bootstrap['events'] if event['finished'] and event['data_checked']}
    standings = {}

    for half, (start, end) in HALVES.items():
        saved = previous.get(half) or {}
        weeks = []
        for gameweek in range(start, end + 1):
            if gameweek not in finalized:
                break
            weeks.append(gameweek)

        if not weeks:
            standings[half] = saved
            continue

        roster = saved.get('roster') or get_players(session, league_id)
        if len(roster) > 39:
            raise RuntimeError("LMS rules cannot leave a single winner with more than 39 players in 19 weeks")

        histories = {}
        for player in roster:
            entry = player['entry']
            history = fetch_json(session, f"https://fantasy.premierleague.com/api/entry/{entry}/history/",
                                 f"entry {entry} history")['current']
            histories[entry] = {week['event']: week for week in history}

        active = list(roster)
        rows = []
        for gameweek in weeks:
            for player in active:
                if gameweek not in histories[player['entry']]:
                    raise RuntimeError(f"Missing GW{gameweek} score for entry {player['entry']}")

            weeks_left = end - gameweek + 1
            boot_count = min(2, max(0, len(active) - weeks_left))

            def ranking(player):
                entry = player['entry']
                result = histories[entry][gameweek]
                coin = hashlib.sha256(f"{league_id}:{start}:{gameweek}:{entry}".encode()).hexdigest()
                return (result['points'] - result['event_transfers_cost'], result['total_points'], coin)

            eliminated = sorted(active, key=ranking)[:boot_count]
            booted = {player['entry'] for player in eliminated}
            active = [player for player in active if player['entry'] not in booted]
            rows.append({'gameweek': gameweek, 'eliminated': eliminated, 'remaining': len(active)})

        standings[half] = {'roster': roster, 'gameweeks': rows, 'winner': active[0] if end in weeks and len(active) == 1 else None}

    return standings


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-l', '--league-id', type=int, required=True,
        help="FPL LMS league ID which to generate standings for.")

    parser.add_argument('-o', '--output', type=str, required=True,
        help="Output file in which to generate the standings.")

    parser.add_argument('-v', '--verbose', action='store_true',
        help="Increase output verbosity.")

    args = parser.parse_args()

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG if args.verbose else logging.INFO)

    output = Path(args.output)
    previous = yaml.safe_load(output.read_text()) if output.exists() else {}
    with requests.Session() as session:
        standings = get_standings(session, args.league_id, previous or {})

    with output.open('w') as file:
        yaml.safe_dump(standings, file, sort_keys=False, allow_unicode=True)