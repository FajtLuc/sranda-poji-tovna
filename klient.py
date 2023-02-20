class Klient:

    def __init__(self, jmeno, prijmeni, vek, telefoni_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefoni_cislo = telefoni_cislo
    def __str__(self):
        return f"Jméno: {self.jmeno}"\
               f"Přijímení: {self.prijmeni}"\
               f"Věk: {self.vek}"\
               f"Telefonní číslo: {self.telefoni_cislo}"