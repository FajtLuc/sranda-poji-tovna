
from klient import Klient

class Seznam:
    print("Vítá vás aplikace srandapojištění.\n")

    def __init__(self):
        self.klient = []

    def legenda(self):
        print("1. Nový pojištěnec")
        print("2. Hledat pojištěnce")
        print("3. Seznam všech pojištěných")
        print("4. Tak zase příště")

    def novy(self):
        jmeno = input("Jak ti říkají? ")
        prijmeni = input("A dál? ")
        vek = int(input("Jak dlouho jsi na světě? "))
        tel_cislo = int(input("Na jaké číslo se ti dovoláme? "))
        pojistenec = Klient(jmeno, prijmeni, vek, tel_cislo)
        self.klient.append(pojistenec)
        print("A už jsi náš")

    def hledat(self):
        jmeno = input("Jméno: ")
        prijmeni = input("Příjmení: ")
        for klient in self.klient:
            if klient.jmeno == jmeno and klient.prijmeni == prijmeni:
                print(pojisteny,"\n")
                break
        else:
            print("Tak toho neznám.\n")

    def vsichni(self):
        for pojistenec in self.klient:
            print(pojistenec,"\n")


    def start(self):

        while True:
            self.legenda()
            volba = input("Cím vám můžu udělat radost?\n")

            if volba == "1":
                self.novy()
            elif volba == "2":
                self.hledat()
            elif volba == "3":
                self.vsichni()
            elif volba == "4":
                print("Sbohem a šáteček.")
                break
            else:
                print("Problém je někde mezi klávesnicí a židlí.\n")

seznam = Seznam()
seznam.start()