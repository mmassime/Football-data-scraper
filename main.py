from Leagues import PremierLeague, SerieA, LaLiga, Bundes, Ligue1

leagues = [PremierLeague(),
           SerieA(),
           LaLiga(),
           Bundes(),
           Ligue1()]
#Print all the tables of the main leagues
for league in leagues:
    print("\n####",league.league_name ,"####\n")
    table = league.get_table()
    print(table)
    print("\nALL THE MATCHES :\n")
    matches = league.get_matches()
    for match in matches:
        print(match)
    print("\nALL THE MATCHES OF FIRST TEAM:\n")
    matches = league.get_matches_team(table[1])
    for match in matches:
        print(match)
    
    

