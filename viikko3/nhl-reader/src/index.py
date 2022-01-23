from audioop import reverse
import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['assists'],
            player_dict['goals'],
            player_dict['team']
        )

        players.append(player)
    
    fin_players = list(filter(lambda p: p.nationality == "FIN", players))

    fin_players.sort(reverse=True)

    for player in fin_players:
        print(player)

if __name__ == "__main__":
    main()
