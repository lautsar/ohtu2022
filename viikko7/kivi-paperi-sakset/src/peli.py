from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_tekoaly import KPSTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja

class Peli:
    @staticmethod
    def kaksinpeli():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def yksinpeli():
        return KPSTekoaly()

    @staticmethod
    def haastava_yksinpeli():
        return KPSParempiTekoaly()