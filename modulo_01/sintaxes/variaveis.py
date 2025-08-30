import modulo


nome_completo = "Maria Clementina"

idade = 24

print(nome_completo)

print("Meu nome é " + nome_completo + " e minha idade é " + str(idade))

#Como idade é um número inteiro (int), ele precisa ser convertido para string usando str() 
# antes de ser concatenado com outras strings.

#Inteiro

numero_inteiro = 3

#Real com ponto flutuante

numero_real = 3.14

print ("soma = ", numero_inteiro + numero_real)
print(numero_real, numero_inteiro)

#type 

print("O tipo da variavel é: ", type(numero_real))

#operadores 

numero1 = 2
numero2 = 3

# multiplicacao

print("2 * 3 = ", numero1 * numero2)

#divisao 

print("2 / 3  = ", numero1 / numero2)
#Para converter para inteiro
print(int(numero1/numero2))

#subtracao

print("2 - 3 =  ", numero1 - numero2)


# Utilizado para calcular o resto da divisão inteira entre dois números. 
# Ele é útil em diversas situações, como determinar se um número 
# é par ou ímpar, trabalhar com ciclos ou intervalos, e muito mais.
print("modulo ", modulo)
