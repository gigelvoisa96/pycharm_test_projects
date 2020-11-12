class Echipa:
    def __init__(self, id, nume, angajati=None, state_de_plata=None):
        self.nume = nume
        self.id = id
        list = []
        if(angajati!=None):
            for elem in angajati:
                list.append(elem)
            self.listaAngajati = list
        list = []
        if(state_de_plata!=None):
            for elem in state_de_plata:
                list.append(elem)
            self.listaState_de_plata = list
