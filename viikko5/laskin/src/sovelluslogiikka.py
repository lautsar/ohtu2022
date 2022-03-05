class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = 0

#    def aseta_arvo(self, arvo):
#        self.tulos = arvo

class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.luku = syote
    
    def suorita(self):
        self.sovelluslogiikka.edellinen = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.tulos = self.sovelluslogiikka.tulos + int(self.luku())

class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.luku = syote
    
    def suorita(self):
        self.sovelluslogiikka.edellinen = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.tulos = self.sovelluslogiikka.tulos - int(self.luku())

class Nollaus:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
    
    def suorita(self):
        self.sovelluslogiikka.edellinen = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.tulos = 0

class Kumoa:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
    
    def suorita(self):
        self.sovelluslogiikka.tulos = self.sovelluslogiikka.edellinen