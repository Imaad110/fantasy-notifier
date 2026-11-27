def find_injured_players(lineup, nfl_players):
    if not lineup or not nfl_players:
        return []

    player_lookup = {}
    for info in nfl_players.values():
        full_name = info.get("full_name")
        team = info.get("team")
        if full_name:
            key = (full_name.strip().lower(), (team or "").strip().upper())
            player_lookup[key] = info

    flagged = []
    for player in lineup:
        name = player.get("name", "").strip()
        team = player.get("team", "").strip().upper()
        position = player.get("position", "")

        match = player_lookup.get((name.lower(), team))
        if not match:
            continue

        # Sleeper leaves injury_status as None when a player is healthy
        status = match.get("injury_status")
        if status:
            flagged.append({
                "name": name,
                "position": position,
                "team": team,
                "status": status,
                "body_part": match.get("injury_body_part") or "Unspecified",
            })

    return flagged


def find_single_player(player_name, nfl_players):
    if not player_name or not nfl_players:
        return None

    target = player_name.strip().lower()
    for info in nfl_players.values():
        full_name = info.get("full_name")
        if full_name and full_name.strip().lower() == target:
            return {
                "name": full_name,
                "position": info.get("position") or "N/A",
                "team": info.get("team") or "FA",
                "status": info.get("injury_status"),
                "body_part": info.get("injury_body_part") or "Unspecified",
            }

    return None


if __name__ == "__main__":
    # Test with sample data so I can verify the parser without waiting on the API
    sample_lineup = [
        {"name": "Jalen Hurts", "position": "QB", "team": "PHI"},
        {"name": "Drake London", "position": "WR", "team": "ATL"},
    ]
    sample_api_data = {
        "1": {"full_name": "Jalen Hurts", "team": "PHI", "injury_status": None},
        "2": {
            "full_name": "Drake London",
            "team": "ATL",
            "injury_status": "Questionable",
            "injury_body_part": "Hip",
        },
    }

    results = find_injured_players(sample_lineup, sample_api_data)
    print(f"Flagged {len(results)} player(s):")
    for p in results:
        print(f"- {p['name']} ({p['position']}, {p['team']}): {p['status']} ({p['body_part']})")
