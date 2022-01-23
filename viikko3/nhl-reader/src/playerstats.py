class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        players = self.reader.players
        nat_players = list(filter(lambda p: p.nationality == nationality, players))
        nat_players.sort(reverse=True)
        
        return nat_players