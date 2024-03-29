from canecas.caneca import Caneca
from canecas.caneca_londres import CanecaLondrina
from canecas.caneca_batman import CanecaBatman
    
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