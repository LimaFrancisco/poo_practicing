from canecas.caneca import Caneca

class CanecaLondrina(Caneca):
    def __init__(self):
        super().__init__("Caneca Londrina", "Cidade de Londres", "Branca") # construtor herdado da classe mãe
        self.bebida = "Chá"
        self.preco = 29.90

    def extras(self):
        print("Como bônus você ganha uma colher")

    def beber(self):
        return "Ta na hora da chá das 5"