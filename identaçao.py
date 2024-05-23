def sacar(self, valor: float) -> None: #metodo q n retorna nd
    if self.saldo >= valor:  #inicio do if
        self.saldo -= valor 
        #fim do if

#fim do metodo


def sacar(valor):
    saldo = 300

    if saldo >= valor:
        print("valor sacado!")

sacar(100)