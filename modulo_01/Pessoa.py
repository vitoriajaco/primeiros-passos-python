class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

##O __str__ permite personalizar a forma como o objeto é exibido quando convertido para string
##   (por exemplo, com print ou str(objeto)).
    def __str__(self):
        return f"Meu nome é {self.nome} e minha idade é {self.idade}"


pessoa = Pessoa("Joaquina Joana", 15)
print(pessoa)