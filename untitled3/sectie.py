class Sectie:
    def __init__(self, id, nume, sef, angajati=None):
        self.nume = nume
        self.id = id
        self.sef = sef
        if(angajati!=None):
            list = []
            for elem in angajati:
                list.append(elem)
            self.listaAngajati = list
