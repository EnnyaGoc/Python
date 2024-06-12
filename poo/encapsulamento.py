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



#property() para criar atributos gerenciados em suas classes.