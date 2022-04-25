from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from kps import KPS

class KPSParempiTekoaly(KPS):
    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self.toinen_pelaaja.anna_siirto()
        self.toinen_pelaaja.aseta_siirto(ensimmaisen_siirto)
        return siirto

    def _toinen_pelaaja(self):
        return TekoalyParannettu(10)
