class Companie:
    def __init__(self, id, nume, sectii=None):
        self.nume = nume
        self.id = id
        if(sectii!=None):
            list = []
            for elem in sectii:
                list.append(elem)
            self.listaSectii = list
    def display(self):
        for elem in self.listaSectii:
            print(elem)