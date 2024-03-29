class Caneca:
    fortato = 'Cilindrico com alça lateral'
    __preco_fabrica = 15

    def __init__(self, nome, logo, cor): # construtor da classe
        self.nome = nome
        self.logo = logo 
        self.cor = cor
        self.status = 'Cheia'
        self.preco = 24.90
    

    def beber(self):
        self.status = 'Vazia'
        return f"É da caneca {self.nome} que eu estou bebendo"

    def encher(self):
        self.status = 'Cheia'
        return f"Estou enchenco a caneca {self.nome}"

class CanecaLondrina(Caneca):
    def __init__(self):
        super().__init__("Caneca Londrina", "Cidade de Londres", "Branca") # construtor herdado da classe mãe
        self.bebida = "Chá"
        self.preco = 29.90

    def extras(self):
        print("Como bônus você ganha uma colher")

    def beber(self):
        return "Ta na hora da chá das 5"

class CanecaBatman(Caneca):
    def __init__(self):
        super().__init__("Caneca Gothan", "Batman", "Preta")
        self.bebida = "Café"
        self.preco = 34.90

    def som(self):
        print("I`m Batman")

    def beber(self):
        return super().beber() + f" {self.bebida}"
    
caneca_londres = CanecaLondrina()
caneca_bylearn = Caneca("Caneca ByLearn", "Foguete da ByLearn", "Branca")
caneca_batman = CanecaBatman()

print(caneca_bylearn.beber())
print(caneca_londres.beber())
print(caneca_batman.beber())

print("PROMOÇÃO")
caneca_bylearn.preco = caneca_bylearn.preco - 5
caneca_londres.preco = caneca_londres.preco - 5
caneca_batman.preco = caneca_batman.preco - 5

print("NOVOS PREÇOS")
print(f"{caneca_bylearn.nome} tem o valor de {caneca_bylearn.preco} reais")
print(f"{caneca_londres.nome} tem o valor de {caneca_londres.preco} reais")
print(f"{caneca_batman.nome} tem o valor de {caneca_batman.preco} reais")