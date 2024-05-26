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

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Qual valor que voce quer depositar? "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"
        else:
            print("valor invalido!")

    elif opcao == "s":        
            valor = float(input("Qual valor voce quer sacar? "))

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

    
    elif opcao == "e":
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(f"""{extrato}
---------------------------------------
        Saldo atual da conta: R${saldo:.2f}
""")

    elif opcao == "q":
        break

    else:
        print("operação inválida, por favor selecione novamente a operação desejada")