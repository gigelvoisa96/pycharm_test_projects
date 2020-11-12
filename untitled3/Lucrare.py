from Echipa import Echipa
class Lucrare:
    def __init__(self, id, nume, total_ore, echipa=None):
        self.nume = nume
        self.id = id
        self.total_ore = total_ore
        if(echipa!=None):
            list = []
            for elem in echipa:
                list.append(elem)
            self.listaEchipa = list
