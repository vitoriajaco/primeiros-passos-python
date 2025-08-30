#Listas a serem trabalhadas
numeros =[]
nomes = ["João", "Joana"]

sobrenomes = ["Souza", "Santos"]

alturas = [1.85, 1.50]

valores_misturados = ["José", 20, 1.85, True]

lista_dentro_da_lista = ["limao", ["laranja", "manga"], "uva"]

frutas = ["morango", "banana", "goiaba", "abacate", "papaya"]



#Manipulando as listas

nomes.extend(sobrenomes) #Adiciona sobrenomes a lista de nomes
numeros.append(2)
lista_dentro_da_lista [0] = "cebola" #Modificando um valor

alturas.append(1.44) #Para adicionar dados no final da lista
alturas.insert(1, 1.20) #Insere um dado num index especifico

frutas.remove("banana")

frutas.pop() #Remove o ultimo elemento
frutas.pop(1) #Remove index especifico


if "Joana" in nomes:
    print("Joana está dentro da lista")
else:
    print("Nao está dentro da lista:")

if __name__ == "__main__":
    print(nomes)
    print(sobrenomes[0])
    print( "Tamanho da lista sobrenomes: ", len(sobrenomes))
    print(alturas[0])
    print(valores_misturados[0])
    print(lista_dentro_da_lista)
    print(alturas)
    print("Numeros ", numeros)
    print("Juntar listas: ", nomes)
    print("Frutas: ", frutas)



