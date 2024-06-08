menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def usuario(nome, data_nasc, cpf, endereço):
    cliente = {"nome": "ana", "data_nasc":"54555436", "cpf":"", "endereço":""}
    

lista = []

for usuario in lista:
    usuario()


















def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R${valor:.2f}\n"      
            
    else:
        print("valor invalido!")
    

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente")
    elif valor > limite:
        print("Passou do limite de valor")
    elif numero_saques > LIMITE_SAQUES:
        print("Passou do limite de saques")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1
    else:
        print("valor invalido!")


def extrato(saldo, /, *, extrato):
    print(f"""{extrato}
---------------------------------------
        Saldo atual da conta: R${saldo:.2f}
""")


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Qual valor que voce quer depositar? "))
        deposito(saldo, valor, extrato)

    elif opcao == "s":        
            valor = float(input("Qual valor voce quer sacar? "))
            saque(saldo="", valor="", extrato="", limite="", numero_saques="", limite_saques="")

            
    elif opcao == "e":
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
           extrato(saldo, extrato="")

    elif opcao == "q":
        break

    else:
        print("operação inválida, por favor selecione novamente a operação desejada")








