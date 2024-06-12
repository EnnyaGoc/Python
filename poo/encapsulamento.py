#para mostrar q algo é privado usa o _ antes
#se acessar o valor de algo privado diretamente nao da erro mas n é o certo

class Conta:
    def __init__(self, nro_agencia, saldo = 0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        #...
        self._saldo += valor

    def sacar(self, valor):
        #...
        self._saldo -= valor

    def mostrar_saldo(self):
        #...
        return self._saldo
    

conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())



#property() para criar atributos gerenciados em suas classes - pode usar esse atributos qndo precisar mudar a implementaçao interna sem alterar a api publica da classe
#no java usa getAtributo, porem no python é mais comum usar o @property
#se nao for modificar o atributo, nem precisa do property


class Foo:
    def __init__(self, x=None):
        self._x = x

    @property #com o @property vc ja tem o aatributo x disponivel na classe
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)
del foo.x
foo.x = 10
print(foo.x)

#------------------------------------------------
class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento
    
pessoa = Pessoa("ana", 1994)
print(f"Nome? {pessoa.nome} \tIdade: {pessoa.idade}")