class Biblioteca:
    def __init__(self, nume, id, sucursale=[]):
        self.nume = nume
        self.id = id
        list = []
        for elem in sucursale:
            list.append(elem)
        self.listaSucursala = list
    def display(self):
        print("-----------BIBLIOTECA---------------------------")
        print("numeBiblioteca: ",self.nume,"id: ",self.id)
        print("\nLista sucursale")
        if self.listaSucursala!=None:
            list = self.listaSucursala
            for elem in list:
                elem.display()
        print("----------END-BIBLIOTECA------------------------")
    def addSucursala(self, sucursala):
        list = []
        list.append(sucursala)
        self.listaSucursala=self.listaSucursala+list
    def addSucursale(self, sucursale=[]):
        list = []
        for elem in sucursale:
            list.append(elem)
        self.listaSucursala = self.listaSucursala+list
