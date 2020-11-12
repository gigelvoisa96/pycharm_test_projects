class Cititor:
    def __init__(self, nr_fisa, nume, adresa, telefon):
        self.nr_fisa = nr_fisa
        self.nume = nume
        self.adresa = adresa
        self.telefon = telefon
    def display(self):
        print("Cititor: ", self.nume, "nr_fisa", self.nr_fisa, "adresa: ", self.adresa, "telefon: ", self.telefon)
