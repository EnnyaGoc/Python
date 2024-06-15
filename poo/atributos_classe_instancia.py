class Estudante:
    escola = "dio"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"



def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("gui", 1)
aluno_2 = Estudante("ana", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "python" #altera pra todos
# aluno_1.escola = "python" altera só pro obj

aluno_3 = Estudante("luis", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)



#---------------------------------------------------------------
#Metodos de classe - tem acesso ao estado da classe (aponta pra classe por meio do parametro), e se chama cls
#Metodos estaticos - tb é vinculado a classe mas n pode acessar ou mudar o estado dela (e nao recebe o parametro)


#se precisar de um contexto da classe, usa o metodo de classe
#se nao precisar de um contexto dela nem do objeto, usado metodo estatico

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
p = Pessoa.criar_de_data_nascimento(2002, 3, 25, "ana")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))

