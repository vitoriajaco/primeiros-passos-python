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

#Formatacao

print("Meu nome é", "Maria", "Sebastiana")

#Que fica diferente quando usa o + 

print("Meu nome é" +  "Maria" + "Sebastiana")

#Forma mais amigavel -> atentar as aspas 
print (f"Nome: {nome} {sobrenome}")

print("Nome: {} {}".format(nome, sobrenome))

print("Nome: %s %s" % (nome, sobrenome))