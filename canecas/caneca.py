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