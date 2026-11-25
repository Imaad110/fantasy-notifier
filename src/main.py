from loader import load_lineup 
from fetcher import fetch_nfl_players
from parser import find_injured_players 
from notifier import print_alerts

def main():
    lineup = load_lineup()
    if not lineup:
        return 
    
    print("Fetching live NFL injury data")
    nfl_players = fetch_nfl_players()
    if not nfl_players:
        print("Could not fetch injury data")
        return 
    flagged_players = find_injured_players(lineup, nfl_players)
    print_alerts(flagged_players)

if __name__ == "__main__":
    main()