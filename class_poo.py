class Caneca:
    fortato = 'Cilindrico com alça lateral'

    def __init__(self, nome, logo, cor): # construtor da classe
        self.nome = nome
        self.logo = logo 
        self.cor = cor
        self.status = 'Cheia'

    def beber(self):
        self.status = 'Vazia'

    def encher(self):
        self.status = 'Cheia'

caneca1 = Caneca("Caneca Londrina", "Cidade de Londres", "Branca")
caneca2 = Caneca("Caneca ByLearn", "Foguete da ByLearn", "Branca")

print(f"A caneca, {caneca1.nome} possui a logo {caneca1.logo}")
print(f"A caneca, {caneca2.nome} possui a logo {caneca2.logo}")

caneca1.beber()
caneca1.encher()

caneca2.beber()

print(f"Caneca 1: {caneca1.status}")
print(f"Caneca 2: {caneca2.status}")

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