from tuomari import Tuomari
from tekoaly import Tekoaly
from kps import KPS

class KPSTekoaly(KPS):  
    def _toisen_siirto(self, ensimmaisen_siirto):
        return self.toinen_pelaaja.anna_siirto()
    
    def _toinen_pelaaja(self):
        return Tekoaly()

