import sys
from loader import load_lineup 
from fetcher import fetch_nfl_players
from parser import find_injured_players, find_single_player
from notifier import print_alerts

def main():
    if len(sys.argv) > 1:
        player_name = " ".join(sys.argv[1:])
        print(f"Fetching live NFL injury data for {player_name}...")
        nfl_players = fetch_nfl_players()
        if not nfl_players:
            print("Could not fetch injury data. Try again later.")
            return

        player = find_single_player(player_name, nfl_players)
        if not player:
            print(f"Could not find '{player_name}' in NFL player data.")
            return

        if player["status"]:
            print_alerts([player])
        else:
            print(f"{player['name']} ({player['position']}, {player['team']}) is healthy.")
        return

    lineup = load_lineup()
    if not lineup:
        return

    print("Fetching live NFL injury data...")
    nfl_players = fetch_nfl_players()
    if not nfl_players:
        print("Could not fetch injury data. Try again later.")
        return

    flagged_players = find_injured_players(lineup, nfl_players)
    print_alerts(flagged_players)

if __name__ == "__main__":
    main()