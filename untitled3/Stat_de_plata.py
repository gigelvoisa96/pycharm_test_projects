from Angajat import Angajat
class Stat_de_plata:
    def __init__(self, id, angajat = Angajat(0, "", "", 0, "", ""), suma = 0):
        self.nume = angajat
        self.id = id
        self.suma = suma
        angajat.salar += suma
