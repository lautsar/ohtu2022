from tuomari import Tuomari
from kps import KPS

class KPSPelaajaVsPelaaja(KPS):
    def _toisen_siirto(self, ensimmaisen_siirto):
        return input("Toisen pelaajan siirto: ")

    def _tulosta_tietokoneen_valinta(self, tokan_siirto):
        return
