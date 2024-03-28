class Caneca:
    fortato = 'Cilindrico com alça lateral'

    def __init__(self, nome, logo, cor): # construtor da classe
        self.nome = nome
        self.logo = logo 
        self.cor = cor
        self.status = 'Cheia'

    def beber(self):
        self.status = 'Vazia'
        return f"É da caneca {self.nome} que eu estou bebendo"

    def encher(self):
        self.status = 'Cheia'
        return f"Estou enchenco a caneca {self.nome}"

class CanecaLondrina(Caneca):
    def __init__(self):
        super().__init__("Caneca Londrina", "Cidade de Londres", "Branca")
        self.bebida = "Chá"

    def extras(self):
        print("Como bônus você ganha uma colher")

    def beber(self):
        self.status = "Vazia" 
        print("Ta na hora da chá das 5")

class CanecaBatman(Caneca):
    def __init__(self):
        super().__init__("Caneca Gothan", "Batman", "Preta")
        self.bebida = "Café"

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

# print(f"A caneca, {caneca1.nome} possui a logo {caneca1.logo}")
# print(f"A caneca, {caneca2.nome} possui a logo {caneca2.logo}")

# print(caneca1.beber())
# print(caneca1.encher())

# print(caneca2.beber())

# print(f"Caneca 1: {caneca1.status}")
# print(f"Caneca 2: {caneca2.status}")

# print(caneca1.fortato)

#     def beber(self):
#         print(f"estou bebendo da caneca {self.nome} ")

# caneca1 = Caneca()

# caneca1.logo = "Logo"
# caneca1.cor = "Verde"
# caneca1.nome = "Teste"

# print(caneca1.logo, caneca1.cor, caneca1.nome)

# caneca1.beber()

# Caneca.logo = 'Padrão' # modificado direto da classe, não é uma boa prática

# caneca2 = Caneca()

# print(caneca2.logo)