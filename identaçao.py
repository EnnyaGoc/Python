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



#Estruturas Condicionais
saldo = 2000
saque = float(input("informe o valor do saque"))

if saldo >= saque:
    print("saque feito")

if saldo < saque:
    print("saldo insuficiente")


if saldo >= saque:
    print("saque feito")

else:
    print("saldo insuficiente")

#else + if = elif

#if ternario
status = "sucesso" if saldo >= saque else "falha"


# Estrutura de Repetição

#for
texto = input("informe um texto")
vogais = "AEIOU"

for letra in texto: #percorrer letra a letra no texto
    if letra.upper() in vogais:
        print(letra, end="")

print()

