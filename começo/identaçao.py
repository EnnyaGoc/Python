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

#------------------------------------------------------


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


#------------------------------------------------------


# Estrutura de Repetição

#for
texto = input("informe um texto")
vogais = "AEIOU"

for letra in texto: #percorrer letra a letra no texto
    if letra.upper() in vogais:
        print(letra, end="")

print()

    # os 2 sao a mesma coisa

for letra in texto: #percorrer letra a letra no texto
    if letra.upper() in vogais:
        print(letra, end="")
else:
    print() #adiciona uma quebra de linha


#Funçao range - funçao built-in do py e é usada cm o for p produzir uma sequencia a partir de um inicio inclusivo e um fim exclusivo

#range(stop) -> range object
#range(start, stop[, step]) -> range object

list(range(4)) #convertendo range p lista p exibir
# [0, 1, 2, 3]



#------------------------------------------------------


# range com for

for numero in range(0, 11):
    print(numero, end=" ") #0 1 2 3 4 5 6 7 8 10


#tabuada do 5
for numero in range(0, 51, 5): #de 5 em 5
    print(numero, end=" ") #0 5 10 15 20 25 30 35 40 45 50



#------------------------------------------------------

#while

opcao = -1

while opcao != 0:
    opcao = int(input("[1] para sacar \n[2] extrato \n[0] para sair"))
    if opcao == 1:
        print("sacando...")
    elif opcao == 2:
        print("exibindo extrato...")


#while com for

opcao = -1

while opcao != 0:
    opcao = int(input("[1] para sacar \n[2] extrato \n[0] para sair"))
    if opcao == 1:
        print("sacando...")
    elif opcao == 2:
        print("exibindo extrato...")

else:
    print("obg, volte sempre!")


#break

while True: #condiçao q sempre vai ser atendida
    numero = int(input("[digite um numero"))

    if numero == 10:
        break

    print(numero)


for numero in range(100):

    if numero == 12:
        break #corta a execuçao

    print(numero, end=" ")



for numero in range(100):

    if numero == 12:
        continue #exibe todos nmenos o 12

    print(numero, end=" ")