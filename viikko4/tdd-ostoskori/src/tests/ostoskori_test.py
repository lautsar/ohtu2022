import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    # 1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    # 2
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    # 3
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_sama_kuin_tuotteen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)
    
    # 4
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        kahvi = Tuote("Kahvi", 5)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kahvi)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    # 5
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_hinta_oikea(self):
        maito = Tuote("Maito", 3)
        kahvi = Tuote("Kahvi", 5)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kahvi)

        self.assertEqual(self.kori.hinta(), 8)
    
    # 6
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_kaksi_tavaraa(self):
        kahvi = Tuote("Kahvi", 5)
        
        self.kori.lisaa_tuote(kahvi)
        self.kori.lisaa_tuote(kahvi)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # 7
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_hinta_oikea(self):
        kahvi = Tuote("Kahvi", 5)
        
        self.kori.lisaa_tuote(kahvi)
        self.kori.lisaa_tuote(kahvi)

        self.assertEqual(self.kori.hinta(), 10)

    # 8
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        kahvi = Tuote("Kahvi", 5)
        self.kori.lisaa_tuote(kahvi)

        ostokset = self.kori.ostokset()
    
        self.assertEqual(len(ostokset), 1)
    
    # 9
    def test_yhden_tuotteen_lisaamisen_jalkeen_oikea_nimi_ja_hinta(self):
        kahvi = Tuote("Kahvi", 5)
        self.kori.lisaa_tuote(kahvi)

        ostos = self.kori.ostokset()[0]
    
        self.assertEqual(ostos.tuote.nimi(), "Kahvi")
        self.assertEqual(ostos.lukumaara(), 1)       

    # 10
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        kahvi = Tuote("Kahvi", 5)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(kahvi)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
    
        self.assertEqual(len(ostokset), 2)

    # 11
    def test_kahden_sama_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos_ja_kaksi_tuotetta(self):
        kahvi = Tuote("Kahvi", 5)
        self.kori.lisaa_tuote(kahvi)
        self.kori.lisaa_tuote(kahvi)

        ostokset = self.kori.ostokset()
    
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(self.kori.tavaroita, 2)
    
    # 12
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoksella_oikea_nimi_ja_maara(self):
        kahvi = Tuote("Kahvi", 5)
        self.kori.lisaa_tuote(kahvi)
        self.kori.lisaa_tuote(kahvi)

        ostos = self.kori.ostokset()[0]
    
        self.assertEqual(ostos.tuote.nimi(), "Kahvi")
        self.assertEqual(ostos.lukumaara(), 2)

    # 13
    def test_korissa_kaksi_samaa_tuotetta_toinen_poistetaan_oikea_maara(self):
        kahvi = Tuote("Kahvi", 5)
        self.kori.lisaa_tuote(kahvi)
        self.kori.lisaa_tuote(kahvi)
        self.kori.poista_tuote(kahvi)

        ostos = self.kori.ostokset()[0]
    
        self.assertEqual(ostos.tuote.nimi(), "Kahvi")
        self.assertEqual(ostos.lukumaara(), 1)
