from Leagues import PremierLeague, SerieA, LaLiga, Bundes, Ligue1

leagues = [PremierLeague('2002-2003'),
           SerieA('1999-2000'),
           LaLiga(),
           Bundes(),
           Ligue1()]
#Print all the tables of the main leagues


print(leagues[0].get_table()[10].get_matches())
    

