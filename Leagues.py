from bs4 import BeautifulSoup
import requests

class League():
    def __init__(self, league_name, league_nb, country, year):
        self.league_name = league_name
        self.league_nb = league_nb
        self.country = country
        self.year = year
        self.teams = self.get_teams()
    
    def get_teams(self):
        """Get all the teams in the league with a code assigned to them by the website"""
        if self.year == 'current':
            html_pl_teams = requests.get(f'https://fbref.com/en/comps/{self.league_nb}/{self.league_name}-Stats').text
        else:
            html_pl_teams = requests.get(f'https://fbref.com/en/comps/{self.league_nb}/{self.year}/{self.year}-{self.league_name}-Stats').text
        soup = BeautifulSoup(html_pl_teams, 'lxml')
        teams_soup = soup.find_all('table', class_='stats_table sortable min_width force_mobilize')[1]
        teams_soup_teams = teams_soup.find_all('a')
        teams = {}

        for team in teams_soup_teams:
            teams[team.text] = team['href'][11:19]
        return teams
 
    def get_table(self):
        '''Return a dict reppresenting the current league table'''
        if self.year == 'current':
            html_pl_teams = requests.get(f'https://fbref.com/en/comps/{self.league_nb}/{self.league_name}-Stats').text
        else:
            html_pl_teams = requests.get(f'https://fbref.com/en/comps/{self.league_nb}/{self.year}/{self.year}-{self.league_name}-Stats').text
        soup = BeautifulSoup(html_pl_teams, 'lxml')
        teams_soup = soup.find_all('table', class_='stats_table sortable min_width force_mobilize')[1]
        teams_soup_teams = teams_soup.find_all('a')
        teams_soup_img = teams_soup.find_all('img')
        teams = {}

        for team, img, i in zip(teams_soup_teams, teams_soup_img, range(1, len(teams_soup_teams)+1)):
            teams[i] = team.text
            """
            img_data = requests.get(img['src']).content 

            with open(f'img/{team.text}.jpg', 'wb') as handler: 

                    handler.write(img_data)
            """
        return teams
    
    def get_matches(self):
        """Get all the matches of the league"""
        if self.year == 'current':
            html_pl_teams = requests.get(f'https://fbref.com/en/comps/{self.league_nb}/schedule/{self.league_name}-Scores-and-Fixtures').text
        else:
            html_pl_teams = requests.get(f'https://fbref.com/en/comps/{self.league_nb}/{self.year}/schedule/{self.year}-{self.league_name}-Scores-and-Fixtures').text
        soup = BeautifulSoup(html_pl_teams, 'lxml')
        row_soup = soup.find_all('tr')
        matches = []
        for tr in row_soup:
            week = tr.find('th', {'data-stat':'gameweek'}).text
            if week and week.isnumeric():
                team1 = tr.find('td', {'data-stat':'home_team'}).text
                team2 = tr.find('td', {'data-stat':'away_team'}).text
                score = tr.find('td', {'data-stat':'score'}).text
                date = tr.find('td', {'data-stat':'date'}).text 
                matches.append((team1, score, team2, week, date))
        return matches
    
    def get_matches_team(self, team : str):
        """Get all the matches of a certain team in the league"""
        if not team in self.teams:
            print("Team not found")
            return []
        if self.year == 'current':
            html_pl_teams = requests.get(f'https://fbref.com/en/squads/{self.teams[team]}/{team}-Stats').text
        else:
            html_pl_teams = requests.get(f'https://fbref.com/en/squads/{self.teams[team]}/{self.year}/{team}-Stats').text
        soup = BeautifulSoup(html_pl_teams, 'lxml')
        table_soup = soup.find('table', id="matchlogs_for")
        row_soup = table_soup.find_all('tr')
        matches = []
        week = 0
        for tr in row_soup:
            league = tr.find('td', {'data-stat':'comp'})
            if league and league.text == self.league_name.replace("-", " "):
                week += 1
                venue = tr.find('td', {'data-stat':'venue'})
                if venue and venue.text == "Home":
                    team1 = team
                    team2 = tr.find('td', {'data-stat':'opponent'}).text
                    gf = tr.find('td', {'data-stat':'goals_for'})
                    ga = tr.find('td', {'data-stat':'goals_against'})
                    if gf:
                        score = f'{gf.text}-{ga.text}'
                    else:
                        score = ''
                    date = tr.find('th', {'data-stat':'date'}).text
                    matches.append((team1, score, team2, week, date))
                else:
                    team1 = tr.find('td', {'data-stat':'opponent'}).text
                    team2 = team
                    ga = tr.find('td', {'data-stat':'goals_for'})
                    gf = tr.find('td', {'data-stat':'goals_against'})
                    if gf:
                        score = f'{gf.text}-{ga.text}'
                    else:
                        score = ''
                    date = tr.find('th', {'data-stat':'date'}).text
                    matches.append((team1, score, team2, week, date))
        return matches
     
class PremierLeague(League):
    def __init__(self, year="current"):
        League.__init__(self, 'Premier-League', '9', 'England', year)

class LaLiga(League):
    def __init__(self, year="current"):
        League.__init__(self, 'La-Liga', '12', 'Spain', year)  

class SerieA(League):
    def __init__(self, year="current"):
        League.__init__(self, 'Serie-A', '11', 'Italy', year)  

class Ligue1(League):
    def __init__(self, year="current"):
        League.__init__(self, 'Ligue-1', '13', 'France', year) 

class Bundes(League): 
    def __init__(self, year="current"):
        League.__init__(self, 'Bundesliga', '20', 'Bundes', year)

