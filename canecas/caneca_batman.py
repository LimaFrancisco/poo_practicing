from canecas.caneca import Caneca

class CanecaBatman(Caneca):
    def __init__(self):
        super().__init__("Caneca Gothan", "Batman", "Preta")
        self.bebida = "Café"
        self.preco = 34.90

    def som(self):
        print("I`m Batman")

    def beber(self):
        return super().beber() + f" {self.bebida}"