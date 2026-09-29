import argparse
import logging
import requests
import yaml


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


MONTHS = {
    'august': (1, 2),
    'september': (3, 5),
    'october': (6, 9),
    'november': (10, 12),
    'december': (13, 18),
    'january': (19, 23),
    'february': (24, 27),
    'march': (28, 30),
    'april': (31, 33),
    'may': (34, 38),
}


def get_winners(session, league_id):
    bootstrap = fetch_json(session, "https://fantasy.premierleague.com/api/bootstrap-static/", "bootstrap")
    finished = {event["id"] for event in bootstrap["events"] if event["finished"] and event["data_checked"]}
    winners = {month: [] for month in MONTHS}
    completed = {month: range(start, end + 1) for month, (start, end) in MONTHS.items()
                 if all(week in finished for week in range(start, end + 1))}
    if not completed:
        return winners

    standings_url = f"https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/"
    players = []
    page = 1
    while True:
        data = fetch_json(session, f"{standings_url}?page_standings={page}", f"standings page {page}")
        players.extend(data["standings"]["results"])
        if not data["standings"]["has_next"]:
            break
        page += 1

    if not players:
        raise RuntimeError("Classic league has no players")

    top_scores = {}
    for player in players:
        entry = player["entry"]
        history = fetch_json(session, f"https://fantasy.premierleague.com/api/entry/{entry}/history/",
                             f"entry {entry} history")["current"]
        scores = {week["event"]: week["points"] - week["event_transfers_cost"] for week in history}
        for month, weeks in completed.items():
            if not all(week in scores for week in weeks):
                raise RuntimeError(f"Missing {month} scores for entry {entry}")
            total = sum(scores[week] for week in weeks)
            if month not in top_scores or total > top_scores[month]:
                top_scores[month] = total
                winners[month] = [player["player_name"]]
            elif total == top_scores[month]:
                winners[month].append(player["player_name"])

    return winners


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-l', '--league-id', type=int, required=True,
        help="FPL classic league ID which to generate monthly winners for.")

    parser.add_argument('-o', '--output', type=str, required=True,
        help="Output file in which to generate the monthly winners.")

    parser.add_argument('-v', '--verbose', action='store_true',
        help="Increase output verbosity.")

    args = parser.parse_args()

    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    with requests.Session() as session:
        winners = get_winners(session, args.league_id)

    with open(args.output, 'w') as output:
        yaml.safe_dump(winners, output, sort_keys=False, allow_unicode=True)