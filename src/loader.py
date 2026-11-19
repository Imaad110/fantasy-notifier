import json

def load_lineup(filepath="data/lineup.json"):
    
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: Could not find lineupe file at '{filepath}'")
        return []
    except json.JSONDecodeError:
        print(f"Error: '{filepath}' is not a valid JSON file")
        return []
    
    players = data.get("players", [])
    if not players:
        print("Warning: Your lineup file is empty. Add players to Lineup.json")
        return []
    
    return players 

if __name__ == "__main__":
    roster = load_lineup()
    print(f"Loaded {len(roster)} players: ")
    for player in roster:
        print(f"- {player['name']} ({player['position']}) {player['team']})")

        