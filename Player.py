class Player():
    def __init__(self, name, team, pos) -> None:
        self.name = name
        self.team = team
        self.pos = pos
    
    def __repr__(self) -> str:
        return self.name + " " + self.pos