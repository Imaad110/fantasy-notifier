# fantasy-notifier
#Fantasy football last-minute injury notifier 

# Project Goal 
As a new user of fantasy football, it's easy to lose games because last-minute injury reports and inactive lists drop right before kickoff when it's too late to change a lineup. Current fantasy apps push generic, cluttered notifications hours in advance, but miss the sudden game-day scratches. This project builds a targeted notification script that pulls live injury feeds and instantly alerts the user to swap locked players before kickoff.

MVP Scope
- Local Configuration (lineup.json): Tracks the user's selected players and roster IDs locally.
- API Integration: Uses Python's requests library to fetch live NFL injury and status feeds from a free sports API.
- **Status Parsing:** Filters incoming JSON data to check if any tracked players are flagged as inactive or injured.
- Alert System:** Triggers terminal or local notifications right before game locks.

## Tech Stack
- Language: Python 
- Libraries: requests, json, datetime
- Data Storage: Local JSON file
- Data Source: Free sports/injury API feed 

## Future Plans
- Integration with desktop push notifications or Twilio SMS alerts.
- Automated lineup fetching directly from fantasy platform APIs.
- Historical tracking of player injury trends and frequency.
