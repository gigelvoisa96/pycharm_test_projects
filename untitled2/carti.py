class Carte:
    def __init__(self, id, titlu, autori, editura ):
        self.id = id
        self.titlu = titlu
        self.autori = autori
        self.editura = editura

    def displayCarte(self):
        print("---------------------")
        print("id:", self.id, "titlu:", self.titlu, "autori:")
        for elem in enumerate(self.autori):
            print(elem)
        print("editura:", self.editura)
        print("---------------------")

