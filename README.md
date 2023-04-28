# Football data scraper
Web scarper to retrieve football data from https://fbref.com/en/

## Requirements:
-   beautifulsoup4=4.12.2
-   requests=2.28.1
-   lxml=4.9.2

## List of available Leagues:
-   Premier League
-   La Liga
-   Serie A
-   Ligue1
-   Bundesliga

## To initialize a league:
```py
from Leagues import PremierLeague

premier_league = PremierLeague()
```
by default you get data from the current year but it's also possible to get data from previous years by passing it to the constructor like this. 

```py
premier_league = PremierLeague('2007-2008')
```

## Methods of a league object:
get_table() : return a dictionary reppresenting the league table.
```py
print(premier_league.get_table())

output = {1: 'Arsenal', 
        2: 'Manchester City', 
        3: 'Newcastle Utd', 
        4: 'Manchester Utd', 
        5: 'Tottenham', 
        6: 'Aston Villa', 
        7: 'Liverpool', 
        8: 'Brighton', 
        9: 'Brentford', 
        10: 'Fulham', 
        11: 'Chelsea', 
        12: 'Crystal Palace', 
        13: 'Wolves', 
        14: 'Bournemouth', 
        15: 'West Ham', 
        16: 'Leeds United', 
        17: "Nott'ham Forest", 
        18: 'Leicester City',
        19: 'Everton', 
        20: 'Southampton'}
```
get_matches() : return a list with all the matches of the league. A match is reppresented by (home_team, score, away_team, gameweek, date)

```py
print(premier_league.get_matches())

output = [('Crystal Palace', '0–2', 'Arsenal', '1', '2022-08-05')
    ('Fulham', '2–2', 'Liverpool', '1', '2022-08-06')
    ('Tottenham', '4–1', 'Southampton', '1', '2022-08-06')
    ('Newcastle Utd', '2–0', "Nott'ham Forest", '1', '2022-08-06')
    ('Leeds United', '2–1', 'Wolves', '1', '2022-08-06')
    ...]
```
get_matches_team(team:str) : return a list with all the matches of a certain team, the format is the same as get_matches().
```py
print(premier_league.get_matches_team('Arsenal'))

output = [('Crystal Palace', '0-2', 'Arsenal', 1, '2022-08-05')
        ('Arsenal', '4-2', 'Leicester City', 2, '2022-08-13')
        ('Bournemouth', '0-3', 'Arsenal', 3, '2022-08-20')
        ('Arsenal', '2-1', 'Fulham', 4, '2022-08-27')
        ('Arsenal', '2-1', 'Aston Villa', 5, '2022-08-31')
        ...]
```
More functions will be added in the future.

