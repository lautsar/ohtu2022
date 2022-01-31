from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.tavaroita = 0
        self.yhteishinta = 0
        self.kokonaisostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return self.tavaroita
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return self.yhteishinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        korissa = False

        for ostos in self.kokonaisostokset:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                korissa = True
                ostos.muuta_lukumaaraa(1)

        if korissa == False:
            self.kokonaisostokset.append(Ostos(lisattava))
        
        self.tavaroita += 1
        self.yhteishinta = self.yhteishinta + lisattava.hinta()

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for ostos in self.kokonaisostokset:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                self.tavaroita -= 1
                self.yhteishinta = self.yhteishinta - poistettava.hinta()

                if ostos.lukumaara() == 0:
                    self.kokonaisostokset.remove(ostos)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kokonaisostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
