class Sucursala:
    def __init__(self, id, nume, adresa):
        self.id = id
        self.nume = nume
        self.adresa = adresa
        self.stoc = []
    def display(self):
        print("---------------SUCURSALA---------------------------------")
        print("id: ", self.id, "nume: ", self.id, "adresa: ", self.adresa)
        print("Stoc:")
        self.displayStoc()
        print("---------------END-SUCURSALA-----------------------------")
    def addCarte(self, carte):
        self.stoc.append(carte)
    def addCarti(self, listaDeCarti):
        self.stoc = self.stoc+listaDeCarti
    def displayStoc(self):
        for elem in self.stoc:
            elem.displayCarte()