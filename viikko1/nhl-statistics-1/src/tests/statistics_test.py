import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_returns_none_when_not_found(self):
        self.assertAlmostEqual(self.statistics.search("Test"), None)
    
    def test_search_returns_player_when_found(self):
        player = self.statistics.search("Semenko")

        self.assertAlmostEqual(player.name, "Semenko")
    
    def test_team_returns_correct_number_of_players(self):
        edm_players = self.statistics.team("EDM")

        self.assertAlmostEqual(len(edm_players), 3)
    
    def test_top_scorers(self):
        best = self.statistics.top_scorers(1)

        self.assertEqual(str(best[0].name), "Gretzky")