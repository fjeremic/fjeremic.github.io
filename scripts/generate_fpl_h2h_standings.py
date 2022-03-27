import argparse
import itertools
import logging
import requests
import yaml

def get_quarter_standings(players, gameweeks):
    standings = []
    for player in players:
        # Initialize the standings where each player is first. We'll fix this after we parse the gameweeks.
        standings.append({
            'rank': 1,
            'teamId': player["entry"],
            'team': player["entry_name"],
            'manager': player["player_name"],
            'wins': 0,
            'draws': 0,
            'losses': 0,
            'points': 0,
            'fplPoints': 0,
        })

    # Parse all wins, draws, losses, and total points, then calculate the points at each iteration
    for gameweek in gameweeks:
        for fixture in gameweek:
            entry_1 = next((x for x in standings if x['teamId'] == fixture["entry_1_entry"]), None)
            entry_2 = next((x for x in standings if x['teamId'] == fixture["entry_2_entry"]), None)

            if not entry_1 or not entry_2:
                raise RuntimeError("Could not extract entires!")
            
            # Append wins
            entry_1['wins'] +=  fixture["entry_1_win"]
            entry_2['wins'] +=  fixture["entry_2_win"]

            # Append draws
            entry_1['draws'] +=  fixture["entry_1_draw"]
            entry_2['draws'] +=  fixture["entry_2_draw"]

            # Append losses
            entry_1['losses'] +=  fixture["entry_1_loss"]
            entry_2['losses'] +=  fixture["entry_2_loss"]

            # Calculate points based off wins and draws
            entry_1['points'] =  entry_1['wins'] * 3 + entry_1['draws']
            entry_2['points'] =  entry_2['wins'] * 3 + entry_2['draws']

            # Append FPL points
            entry_1['fplPoints'] +=  fixture["entry_1_points"]
            entry_2['fplPoints'] +=  fixture["entry_2_points"]

    # Sort the standings first by points then by FPL points
    standings.sort(key = lambda x: (x['points'], x['fplPoints']), reverse = True)

    # Now that we are sorted update the true ranking in order
    for i in range(len(standings)):
        standings[i]['rank'] = i + 1

    return standings

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-l', '--league-id', type=int, required=True,
        help="FPL H2H league ID which to generate standings for.")

    parser.add_argument('-o', '--output', type=str, required=True,
        help="Output file in which to generate the standings.")

    parser.add_argument('-v', '--verbose', action='store_true',
        help="Increase output verbosity.")

    global args
    args = parser.parse_args()

    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    session = requests.Session()

    logging.debug("Fetching standings")
    data = session.get(f"https://fantasy.premierleague.com/api/leagues-h2h/{args.league_id}/standings").json()

    # Parse all the players
    players = data["standings"]["results"]

    # Parse all the gameweeks fixtures
    fixtures = []
    fixtures_url = f"https://fantasy.premierleague.com/api/leagues-h2h-matches/league/{args.league_id}/?page={{:d}}"

    for page in itertools.count(1):
        logging.debug(f"Fetching fixtures on page {page}")
        page_data = session.get(fixtures_url.format(page)).json()["results"]

        if page_data:
            fixtures.extend(page_data)
        else:
            break

    if len(fixtures) != 38 * (len(players) // 2):
        raise RuntimeError(f"Invalid number of fixtures ({len(fixtures)}) parsed for ({len(players)}) number of players")


    logging.debug(f"Computing gameweeks")

    gameweeks = []
    for i in range(38):
        gameweeks.append(fixtures[i * (len(players) // 2) : (i + 1) * (len(players) // 2)])

    logging.debug(f"Calculating quarter standings")

    q1_standings = get_quarter_standings(players, gameweeks[0:10])
    q2_standings = get_quarter_standings(players, gameweeks[10:19])
    q3_standings = get_quarter_standings(players, gameweeks[19:29])
    q4_standings = get_quarter_standings(players, gameweeks[29:38])

    fpl_h2h_standings = {
        'q1': q1_standings,
        'q2': q2_standings,
        'q3': q3_standings,
        'q4': q4_standings,
    }

    logging.debug(f"Generating output to {args.output}")
    
    with open(args.output, 'w') as f:
        class IndentListDumper(yaml.Dumper):
            def increase_indent(self, flow=False, indentless=False):
                return super(IndentListDumper, self).increase_indent(flow, False)

        yaml.dump(fpl_h2h_standings, f, Dumper=IndentListDumper, sort_keys=False)
