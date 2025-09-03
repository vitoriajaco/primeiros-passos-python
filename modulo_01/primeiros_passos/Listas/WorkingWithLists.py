#Criando lista aninhada

alunos = [
    ["Nome", "Genero", "Escolaridade"], #0
    ["Ana", "Feminino", "Fundamental 1"], #1
    ["Maria", "Feminino", "Fundamental 3"], #2
    ["Pedro", "Masculino", "Ensino Medio"], #3
    # 0         #1            #3
]

x = [alunos[1][0], alunos[2][0], alunos[3][0]]

print(alunos[3] [0])
print("Alunos:", alunos[1][0], alunos[2][0], alunos[3][0])

print(x.index("Maria"))
print(x)

#Percorrendo lista de maneira simples e baguncada
for lista in alunos:
    for dados in lista:
        print(dados, end=" ")
    print()

for dados in alunos[1:]:
    nome, genero, escolaridade = dados
    print(f"{nome} é do sexo {genero} e está no {escolaridade}")
