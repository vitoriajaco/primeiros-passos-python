#Lista

carros = ["gol", "corsa", "monza", "santana", "fusca", "hb20"]

#Percorrendo lista com for:

for carro in range(len(carros)):
    print("Percorrendo o indice de carro ", carro)

for carro in carros:
    print("O nome do carro é: ", carro)

contador = 0
while contador < len(carros):
    print("Contando o carro ", contador)
    contador += 1

#Fatiando Listas
print(carros, "Lista completa")
print(carros[1:4], "Do indice 1 ao 3")
print(carros[::2], "Todos pulando de 2 em 2")
print(carros[::-1], "Inverte a lista")
