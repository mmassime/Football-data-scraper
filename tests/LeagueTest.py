#change the imported league with the one to test
from Leagues import BrazilianSerieA as league

test_league = league()
table = test_league.get_table()
print("=====TABLE=====")
print(table)
print("=====TEAMS=====")
print(test_league.get_teams())
print("=====MATCHES=====")
print(test_league.get_matches())
print("=====MATCHES(1st in the league)=====")
print(test_league.get_matches_team(table[1].name))
print("=====PLAYERS(1st in the league)=====")
print(table[1].get_players())
