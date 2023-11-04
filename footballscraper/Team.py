from bs4 import BeautifulSoup
import requests
from .Player import Player
import time

class Team():
    def __init__(self, name, code, league, year='current') -> None:
        self.name = name
        self.code = code
        self.league = league
        self.year = year
    
    def get_matches(self):
        if self.year == 'current':
            html_pl_teams = requests.get(f'https://fbref.com/en/squads/{self.code}/{self.name}-Stats').text
        else:
            html_pl_teams = requests.get(f'https://fbref.com/en/squads/{self.code}/{self.year}/{self.name}-Stats').text
        time.sleep(0.5)
        soup = BeautifulSoup(html_pl_teams, 'lxml')
        table_soup = soup.find('table', id="matchlogs_for")
        row_soup = table_soup.find_all('tr')
        matches = []
        week = 0
        for tr in row_soup:
            league = tr.find('td', {'data-stat':'comp'})

            if league and league.text in self.league.league_name.replace("-", " "):
                week += 1
                venue = tr.find('td', {'data-stat':'venue'})
                if venue and venue.text == "Home":
                    team1 = self.name
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
                    team2 = self.name
                    ga = tr.find('td', {'data-stat':'goals_for'})
                    gf = tr.find('td', {'data-stat':'goals_against'})
                    if gf:
                        score = f'{gf.text}-{ga.text}'
                    else:
                        score = ''
                    date = tr.find('th', {'data-stat':'date'}).text
                    matches.append((team1, score, team2, week, date))
        return matches
    
    def get_players(self):
        if self.year == 'current':
            html_team = requests.get(f'https://fbref.com/en/squads/{self.code}/{self.name}-Stats').text
        else:
            html_team = requests.get(f'https://fbref.com/en/squads/{self.code}/{self.year}/{self.name}-Stats').text
        time.sleep(0.5)
        soup = BeautifulSoup(html_team, 'lxml')
        team_soup = soup.find('tbody')
        player_soup = team_soup.find_all('tr')
        players = {}
        for player in player_soup:
            name = player.find('th', {'data-stat':'player'}).text
            team = self.name
            pos = player.find('td', {'data-stat':'position'}).text
            players[name] = Player(name, team, pos)
        return players        

    def get_logo(self, path=""):
        html_team = requests.get(f'https://fbref.com/en/squads/{self.code}/{self.name}-Stats').text
        time.sleep(0.5)
        soup = BeautifulSoup(html_team, 'lxml')
        teams_soup_img = soup.find('img', class_="teamlogo")
        img_data = requests.get(teams_soup_img['src']).content 
        time.sleep(0.5)
        with open(f'{path}{self.name}.jpg', 'wb') as handler: 
                handler.write(img_data)
                
    def __repr__(self) -> str:
        return self.name