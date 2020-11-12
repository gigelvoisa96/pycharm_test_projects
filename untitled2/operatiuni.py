class Operatiune:
    def __init__(self, biblioteca, sucursala, carte, cititor, actiune, data_imprumutare, data_returnare):
        if actiune=="imprumut":
            self.timp_imprumut = "21-00-00"
        elif actiune=="returnare":
            self.timp_imprumut = "00-00-00"
        self.biblioteca = biblioteca
        self.sucursala = sucursala
        self.carte = sucursala
        self.carte = carte
        self.cititor = cititor
        self.actiune = actiune
        self.data_imprumutare = data_imprumutare
        self.data_returnare = data_returnare
        data = self.timp_imprumut.split("-",3)
        print(data[0], data[1], data[2])
    def display(self):
        print("actiunea de ", self.actiune, "a cartii:")
        self.carte.displayCarte()
        print("s-a realizat intre")
        self.biblioteca.display()
        print("cu sucursala:")
        self.sucursala.display()
        print("cititorul:")
        self.cititor.display()
    def setDataImprumutare(self):
        return 