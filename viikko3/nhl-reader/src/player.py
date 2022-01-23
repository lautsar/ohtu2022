class Player:
    def __init__(self, name, nationality, assists, goals, team):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.team = team
    
    def __str__(self):
        return f"{self.name:20} {self.team} {str(self.goals):2} + {str(self.assists):2} = {str(self.goals+self.assists):3}"
    
    def __lt__(self, other):
        if (self.goals + self.assists) == (other.goals + other.assists):
            return self.goals < other.goals
        else:
            return (self.goals + self.assists) < (other.goals + other.assists)

