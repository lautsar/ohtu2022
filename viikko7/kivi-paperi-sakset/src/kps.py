from tuomari import Tuomari
#from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
#from kps_tekoaly import KPSTekoaly
#from kps_parempi_tekoaly import KPSParempiTekoaly

class KPS:
    def __init__(self):
        self.tuomari = Tuomari()
        self.toinen_pelaaja = self._toinen_pelaaja()

    def pelaa(self):
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        self._tulosta_tietokoneen_valinta(tokan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self.tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

            self._tulosta_tietokoneen_valinta(tokan_siirto)

        print("Kiitos!")
        print(self.tuomari)

    def _ensimmaisen_siirto(self):
      return input("Ensimmäisen pelaajan siirto: ")

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

    def _toinen_pelaaja(self):
        return None

    def _tulosta_tietokoneen_valinta(self, tokan_siirto):
        print(f"Tietokone valitsi: {tokan_siirto}")


