from Companie import Companie
from sectie import Sectie
from Lucrare import Lucrare
from Echipa import Echipa
from  Angajat import Angajat
from Stat_de_plata import Stat_de_plata
def main():
    angajat11 = Angajat(1, "Andrei", "str. Floriilor", 2400, "m", "1/1/1996")
    angajat12 = Angajat(2, "Andrei", "str. Floriilor", 2300, "m", "1/2/1995")
    angajat13 = Angajat(3, "Andrei", "str. Floriilor", 2200, "m", "2/1/1995")
    angajat14 = Angajat(4, "Andrei", "str. Floriilor", 2600, "m", "2/2/1992")
    angajat15 = Angajat(5, "Andrei", "str. Floriilor", 2500, "m", "4/4/1994")
    angajat21 = Angajat(6, "Andrei", "str. Floriilor", 2400, "m", "1/1/1996")
    angajat22 = Angajat(7, "Andrei", "str. Floriilor", 2300, "m", "1/2/1995")
    angajat23 = Angajat(8, "Andrei", "str. Floriilor", 2200, "m", "2/1/1995")
    angajat24 = Angajat(9, "Andrei", "str. Floriilor", 2600, "m", "2/2/1992")
    angajat25 = Angajat(10, "Andrei", "str. Floriilor", 2500, "m", "4/4/1994")
    angajat31 = Angajat(11, "Andrei", "str. Floriilor", 2400, "m", "1/1/1996")
    angajat32 = Angajat(12, "Andrei", "str. Floriilor", 2300, "m", "1/2/1995")
    angajat33 = Angajat(13, "Andrei", "str. Floriilor", 2200, "m", "2/1/1995")
    angajat34 = Angajat(14, "Andrei", "str. Floriilor", 2600, "m", "2/2/1992")
    angajat35 = Angajat(15, "Andrei", "str. Floriilor", 2500, "m", "4/4/1994")
    angajat41 = Angajat(16, "Andrei", "str. Floriilor", 2400, "m", "1/1/1996")
    angajat42 = Angajat(17, "Andrei", "str. Floriilor", 2300, "m", "1/2/1995")
    angajat43 = Angajat(18, "Andrei", "str. Floriilor", 2200, "m", "2/1/1995")
    angajat44 = Angajat(19, "Andrei", "str. Floriilor", 2600, "m", "2/2/1992")
    angajat45 = Angajat(20, "Andrei", "str. Floriilor", 2500, "m", "4/4/1994")
    angajat51 = Angajat(21, "Andrei", "str. Floriilor", 2400, "m", "1/1/1996")
    angajat52 = Angajat(22, "Andrei", "str. Floriilor", 2300, "m", "1/2/1995")
    angajat53 = Angajat(23, "Andrei", "str. Floriilor", 2200, "m", "2/1/1995")
    angajat54 = Angajat(24, "Andrei", "str. Floriilor", 2600, "m", "2/2/1992")
    angajat55 = Angajat(25, "Andrei", "str. Floriilor", 2500, "m", "4/4/1994")
    sef1 = angajat14
    sef2 = angajat24
    sef3 = angajat34
    sef4 = angajat44
    sef5 = angajat54

    sectie1 = Sectie(1, "Sectie1", sef1, [angajat11, angajat12, angajat13, angajat14, angajat15])
    sectie2 = Sectie(2, "Sectie2", sef2, [angajat21, angajat22, angajat23, angajat24, angajat25])
    sectie3 = Sectie(3, "Sectie3", sef3, [angajat31, angajat32, angajat33, angajat34, angajat35])
    sectie4 = Sectie(4, "Sectie4", sef4, [angajat41, angajat42, angajat43, angajat44, angajat45])
    sectie5 = Sectie(5, "Sectie5", sef5, [angajat51, angajat52, angajat53, angajat54, angajat55])

    state_de_plata1 = [Stat_de_plata(1, angajat11, 1100), Stat_de_plata(6, angajat21, 1200),
                       Stat_de_plata(11, angajat31, 1300), Stat_de_plata(16, angajat41, 1400),
                       Stat_de_plata(21, angajat51, 1500)]
    state_de_plata2 = [Stat_de_plata(2, angajat12, 1100), Stat_de_plata(7, angajat22, 1200),
                       Stat_de_plata(12, angajat32, 1300), Stat_de_plata(17, angajat42, 1400),
                       Stat_de_plata(22, angajat52, 1500)]
    state_de_plata3 = [Stat_de_plata(3, angajat13, 1100), Stat_de_plata(8, angajat23, 1200),
                       Stat_de_plata(13, angajat33, 1300), Stat_de_plata(18, angajat43, 1400),
                       Stat_de_plata(23, angajat53, 1500)]
    state_de_plata4 = [Stat_de_plata(4, angajat14, 1100), Stat_de_plata(9, angajat24, 1200),
                       Stat_de_plata(14, angajat34, 1300), Stat_de_plata(19, angajat44, 1400),
                       Stat_de_plata(24, angajat54, 1500)]
    state_de_plata5 = [Stat_de_plata(5, angajat15, 1100), Stat_de_plata(10, angajat25, 1200),
                       Stat_de_plata(15, angajat35, 1300), Stat_de_plata(20, angajat45, 1100),
                       Stat_de_plata(25, angajat55, 1500)]

    companie = Companie(1, "Companie1", [sectie1, sectie2, sectie3, sectie4, sectie5])
    echipa1 = Echipa(1, "ech1", [angajat11, angajat21, angajat31, angajat41, angajat51], state_de_plata1)
    echipa2 = Echipa(2, "ech2", [angajat12, angajat22, angajat32, angajat42, angajat52], state_de_plata2)
    echipa3 = Echipa(3, "ech3", [angajat13, angajat23, angajat33, angajat43, angajat53], state_de_plata3)
    echipa4 = Echipa(4, "ech4", [angajat14, angajat24, angajat34, angajat44, angajat54], state_de_plata4)
    echipa5 = Echipa(5, "ech5", [angajat15, angajat25, angajat35, angajat45, angajat55], state_de_plata5)
    proiect1 = Lucrare(1, "lucrare1", 240,
                       Echipa(1, "ech1", [angajat11, angajat21, angajat31, angajat41, angajat51], state_de_plata1))
    proiect2 = Lucrare(2, "lucrare2", 240,
                       Echipa(2, "ech2", [angajat12, angajat22, angajat32, angajat42, angajat52], state_de_plata2))
    proiect3 = Lucrare(3, "lucrare3", 240,
                       Echipa(3, "ech3", [angajat13, angajat23, angajat33, angajat43, angajat53], state_de_plata3))
    proiect4 = Lucrare(4, "lucrare4", 240,
                       Echipa(4, "ech4", [angajat14, angajat24, angajat34, angajat44, angajat54], state_de_plata4))
    proiect5 = Lucrare(5, "lucrare5", 240,
                       Echipa(5, "ech5", [angajat15, angajat25, angajat35, angajat45, angajat55], state_de_plata5))

if __name__ == "__main__": main()
