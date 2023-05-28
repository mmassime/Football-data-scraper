from bs4 import BeautifulSoup
from Team import Team
import requests
import time

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
        time.sleep(0.5)
        soup = BeautifulSoup(html_pl_teams, 'lxml')
        teams_soup = soup.find_all('table', class_='stats_table sortable min_width force_mobilize')[1]
        teams_soup_teams = teams_soup.find_all('a')
        teams = {}

        for team in teams_soup_teams:
            teams[team.text] = Team(team.text, team['href'][11:19], self, self.year)
        return teams
 
    def get_table(self):
        '''Return a dict reppresenting the current league table'''
        if self.year == 'current':
            html_pl_teams = requests.get(f'https://fbref.com/en/comps/{self.league_nb}/{self.league_name}-Stats').text
        else:
            html_pl_teams = requests.get(f'https://fbref.com/en/comps/{self.league_nb}/{self.year}/{self.year}-{self.league_name}-Stats').text
        time.sleep(0.5)
        soup = BeautifulSoup(html_pl_teams, 'lxml')
        teams_soup = soup.find_all('table', class_='stats_table sortable min_width force_mobilize')[1]
        teams_soup_teams = teams_soup.find_all('a')
        teams_soup_img = teams_soup.find_all('img')
        teams = {}

        for team, img, i in zip(teams_soup_teams, teams_soup_img, range(1, len(teams_soup_teams)+1)):
            teams[i] = self.teams[team.text]
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
        time.sleep(0.5)
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
        return self.teams[team].get_matches()
        
     
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

