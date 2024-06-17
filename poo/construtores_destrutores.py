#metodo construtor - sempre executado qndo a nova instancia da classe é criada. Nele tem o estado inicializado do objeto (__init__)

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

#metodo destrutor - sempre executado qndo uma instancia é destruída(__del__)

    def __del__(self):
        print("destruindo a instancia")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("zeus", "branco e preto", False)
    print(c.nome)


c = Cachorro("mel", "amarelo")
c.falar

print("ola mundo")

#a palavra del vc usa pra forçar a exclusao
del c

print("ola mundo")
print("ola mundo")


#criar_cachorro()
