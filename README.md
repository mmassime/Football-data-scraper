# Football data scraper
Web scarper to retrieve football data from https://fbref.com/en/

Attention: if the website detects too many requests per minute it might block you for 1 hour. To avoid that a time sleep of 0.5 seconds has been added after every request.



## Requirements:
-   beautifulsoup4=4.12.2
-   requests=2.28.1
-   lxml=4.9.2

## List of available Leagues:
-   Premier League (ENG)
-   Championship (ENG)
-   La Liga (SPA)
-   Serie A (ITA)
-   Ligue1 (FRA)
-   Bundesliga (GER)
-   Jupiler Pro League (BEL)
-   Eredivisie (NET)
-   Série A (BRA)
-   Liga MX (MEX)
-   Primeira Liga (POR)
-   Primera Division (ARG)
-   Saudi Pro League (SAU)
-   Scottish Premiership (SCO)


## To initialize a league:
```py
from Leagues import PremierLeague

premier_league = PremierLeague()
```
by default you get data from the current year but it's also possible to get data from previous years by passing it to the constructor like this. 

```py
premier_league = PremierLeague('2007-2008')
```

## Methods of a League object:
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
get_teams() : return a dictionary with as key the name of each team in the league and as value an object of the class Team.
```py
print(premier_league.get_teams())

output = {'Manchester City': Manchester City, 
        'Arsenal': Arsenal, 
        'Manchester Utd': Manchester Utd, 
        'Newcastle Utd': Newcastle Utd, 
        'Liverpool': Liverpool... }
```

## Methods of a Team object:
How to acces a team
```py
from Leagues import SerieA

serie_a = SerieA()
lazio = serie_a.get_teams()['Lazio']
```
get_matches() : return a list with all the matches of the team, the format is the same as get_matches() of the League object.
```py
print(lazio.get_matches())

output = [('Lazio', '2-1', 'Bologna', 1, '2022-08-14'),
        ('Torino', '0-0', 'Lazio', 2, '2022-08-20'), 
        ('Lazio', '3-1', 'Inter', 3, '2022-08-26'), 
        ('Sampdoria', '1-1', 'Lazio', 4, '2022-08-31'), 
        ('Lazio', '1-2', 'Napoli', 5, '2022-09-03')...]
```
get_payers() : return a dictionary with as key the name of each player in the team and as value an object of the class Player.
```py
print(lazio.get_players())

output = {'Ivan Provedel': Ivan Provedel GK, 
        'Felipe Anderson': Felipe Anderson FW, 
        'Sergej Milinković-Savić': Sergej Milinković-Savić MF, 
        'Mattia Zaccagni': Mattia Zaccagni FW, 
        'Alessio Romagnoli': Alessio Romagnoli DF, 
        'Adam Marušić': Adam Marušić DF...}
```
get_logo(path) : save the logo of the team as a jpg in a specified folder.
```py
import os
from Leagues import PremierLeague, SerieA, LaLiga, Bundes, Ligue1

#save all the logos of the teams in the major leagues
leagues = [PremierLeague(), SerieA(), LaLiga(), Bundes(), Ligue1()]
for league in leagues:
    #create a folder with the name of the league inside folder img
    os.mkdir(f"img/{league.league_name}")
    #loop trhough the teams in the league and save their logo
    for team in league.get_teams().values():
        team.get_logo(f"img/{league.league_name}/")
```
## Methods of a Player object:
to be added.

## Problems:
- Some leagues that use playoff may have problems when showing matches 
- If any other problem is found please open an issue


More functions will be added in the future.

