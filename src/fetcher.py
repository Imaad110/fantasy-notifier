import requests 

NFL_PLAYERS_URL = "https://api.sleeper.app/v1/players/nfl"

def fetch_nfl_players():
    try: 
        response = requests.get(NFL_PLAYERS_URL, timeout=15)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.Timeout:
        print("Error: Request timed out while fetching NFL players.")
        return {}
    except requests.exceptions.ConnectionError:
        print(f"Error: Failed to fetch NFL player data.")
        return {}
    except ValueError:
        print("Error: Received invalid JSON from the NFL API.")
        return {}


if __name__ == "__main__":
    print("Fetching live NFL player data")
    players = fetch_nfl_players()
    if players:
        print(f"Successfully fetched {len(players)} players. ")
        for info in players.values():
            if info.get("injury_status"):
                print (
                    f"Sample injured player: {info.get('full_name')} "
                    f"({info.get('team')}) - {info.get('injury_status')}"
                )
                break