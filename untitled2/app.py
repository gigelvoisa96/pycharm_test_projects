from biblioteca import Biblioteca
from carti import Carte
from sucursala import Sucursala
from operatiuni import Operatiune
from cititori import Cititor
biblio = Biblioteca("Petre Dulfu", 1)
biblio.display()
succurs = Sucursala(1,"Filiara Principala","Bulvardul Independentei")
biblio.addSucursala(succurs)
sucursalaIorga = Sucursala(2, "Filiara Nicolae Iorga", "str. Nicolae Iorga")
sucursalaTehnica = Sucursala(3, "Filiara Stiinte", "str. Victoriei")
biblio.addSucursale([sucursalaIorga, sucursalaTehnica])
biblio.display()
#self, id, titlu, autori, editura
carte1 = Carte(1, "Amintiri", ["Ion Creanga", "Slavici", "Eminescu"], "Ed. Junimea")
#carte1.displayCarte()
carte2 = Carte(2, "Povestiri", ["Petre Dulfu"], "Transilvania")
carte3 = Carte(3, "Schita", ["I.L.Caragiale"], "Junimea")
succurs.addCarti([carte1, carte2, carte3])
sucursalaTehnica.addCarti([carte1, carte3])
sucursalaIorga.addCarti([carte2, carte3])
biblio.display()
#------------------------------------
cititor1 = Cititor(1, "ana","str. Florilor", "0756403345")
cititor2 = Cititor(2, "eugen", "str. Transilvaniei", "0756456908")
cititor3 = Cititor(3, "elena", "str. Victoriei", "0744567890")
imprumut1 = Operatiune(biblio, succurs, carte1, cititor1, "imprumut")
imprumut2 = Operatiune(biblio, sucursalaIorga, carte2, cititor2, "imprumut")
imprumut3 = Operatiune(biblio, sucursalaTehnica, carte3, cititor3, "imprumut")
imprumut4 = Operatiune(biblio, succurs, carte2, cititor2, "imprumut")