#Declaracao

nome_completo = "Maria Joaquina do Amaral Pereira Goes"


#Dessa forma da pra quebrar em linhas
nome_com_aspas = """Maria 

Elismando

da 

Silva"""

print(nome_completo)

print(nome_com_aspas)

nome = "Lupércio"
sobrenome = "Santos"

#Se a letra não estiver presente ele retornará -1
#o find mostra em que posicao está do index
a = nome.find("i")
print(a)

#Para substituir uma letra por outra
sobrenome = sobrenome.replace("o", "e")
print(sobrenome)

telefone = "(87)99991534"
telefone = telefone.replace("(","",).replace(")","",)
print(telefone)
#Formatacao

print("Meu nome é", "Maria", "Sebastiana")

#Que fica diferente quando usa o + 

print("Meu nome é" +  "Maria" + "Sebastiana")

#Forma mais amigavel -> atentar as aspas 
print (f"Nome: {nome} {sobrenome}")

print("Nome: {} {}".format(nome, sobrenome))

print("Nome: %s %s" % (nome, sobrenome))