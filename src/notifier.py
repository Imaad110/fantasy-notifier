from datetime import datetime 

def print_alerts(flagged_players):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Injury check ({timestamp})")

    if not flagged_players:
        print("All good! None of your players are flagged")
        return
    print(f"Warning: {len(flagged_players)} of your players are flagged for injury")
    for player in flagged_players:
        print(f"- {player['name']} ({player['position']}, {player['team']}): {player['status']} - {player['body_part']}")

if __name__ == "__main__":
    print("Test 1 (Healthy):")
    print_alerts([])

    print("\nTest 2 (Injured):")
    sample_flagged = [
        {
            "name": "Drake London",
            "position": "WR",
            "team": "ATL",
            "status": "Questionable",
            "body_part": "Hip"
        }
    ]
    print_alerts(sample_flagged)