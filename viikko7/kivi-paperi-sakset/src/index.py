from peli import Peli

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            peli = Peli.kaksinpeli()
        elif vastaus.endswith("b"):
            peli = Peli.yksinpeli()
        elif vastaus.endswith("c"):
            peli = Peli.haastava_yksinpeli()
        else:
            break

        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
        peli.pelaa()

if __name__ == "__main__":
    main()
