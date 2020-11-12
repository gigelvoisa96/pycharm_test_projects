class Banci:
	def __init__(self, nume_banca, cod_banca):
	  self.nume_banca = nume_banca
	  self.cod_banca = cod_banca

class Sucursale:
	def __init__(self, banca, codBancar, adresa):
		self.banca = Banci(banca, codBancar)
		self.adresa = adresa

class Clienti:
	def __init__(self, nume, adresa, numeBanca, codBancar, adresaBanca):
		self.nume = nume
		self.adresa = adresa
		self.sucursa = Sucursale(numeBanca, codBancar, adresaBanca)

class Depozit:
	def __init__(self, tip_bani):
		self.tip_moneda = tip_bani
	def getDepozit(self):
		return self;

class Curent:
	def __init__(self, tip_bani):
		self.tip_moneda = tip_bani
	def getCurent(self):
		return self;

class Conturi:
	def __init__(self, iban, nume, adresa, numeBanca, codBancar, adresaBanca, tip_cont, tip_bani):
		self.client = Clienti(nume, adresa, numeBanca, codBancar, adresaBanca)
		self.iban = iban
		self.sold = 0
		if tip_cont == "depozit" : self.tip = Depozit(tip_bani)
		if tip_cont == "curent" : self.tip = Curent(tip_bani)
	def __str__(self):
		return "<Cont iban:%s cu sold:%s>" % (self.iban, self.sold)
	def tranzactionare(self, valoare):
		self.sold = self.sold+valoare
	def displaySold(self, ):
		print ("Clientul " + self.client.nume + "are " + self.sold)
	def getIban(self ):
		return self.iban

class Tranzactii:
	def __init__(self,
				numeEmitator, adresaEmitator,  iban_contEmitator, numeBancaEmitator, codBancarEmitator, adresaBancaEmitator,
				numeReceptor, adresaReceptor, iban_contReceptor, numeBancaReceptor, codBancarReceptor, adresaBancaReceptor):
        #self, iban, nume, adresa, numeBanca, codBancar, adresaBanca, tip_cont, tip_bani
		self.contEmitator = Conturi(iban_contEmitator, numeEmitator, adresaEmitator, numeBancaEmitator, codBancarEmitator, adresaBancaEmitator, "depozit", "lei")
		self.contReceptor = Conturi(iban_contReceptor, numeReceptor, adresaReceptor, numeBancaReceptor, codBancarReceptor, adresaBancaReceptor, "depozit", "lei")
	def depuneri(self, suma):
		self.contEmitator.tranzactionare(+suma)
	def retrageri(self, suma):
		self.contEmitator.tranzactionare(-suma)
	def transfer(self, suma):
		self.contEmitator.tranzactionare(-suma)
		self.contReceptor.tranzactionare(suma)
	def getCont(self, iban_cont):
		if(iban_cont==self.contEmitator.getIban()):
			return self.contEmitator
		elif(iban_cont==self.contReceptor.getIban()):
			return self.contReceptor

#end_classes
#begin_main
#numeEmitator, adresaEmitator,  iban_contEmitator, numeBancaEmitator, codBancarEmitator, adresaBancaEmitator,
#numeReceptor, adresaReceptor, iban_contReceptor, numeBancaReceptor, codBancarReceptor, adresaBancaReceptor 
tranzactie = Tranzactii("ana", "Str. a", "2000102", "Banca Transilvania", "4444","str AAA", "andrei", "Str. b", "39227001", "BCR", "3456", "str BBB")
tranzactie.depuneri(20020)
tranzactie.retrageri(38383)
tranzactie.transfer(3004)
contAfis = tranzactie.getCont("2000102")
print (str(contAfis))
contAfis = tranzactie.getCont("39227001")
print (str(contAfis))
#ContAfis.displaySold()
#end_main