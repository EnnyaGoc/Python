valor = 0
extrato = ""
saldo = 0
limite_saque = 500
qtd_saque = 0


while True:
    opcao = input('''Digite:
1 - Depositar
2 - Sacar
3 - Ver extrato
4 - Sair
      ''')

    
    if opcao == "1":
        valor = float(input("Quanto voce quer depositar? "))
        if valor > 0:
            saldo = saldo + valor
            extrato = extrato + f"Depósito: R$ {valor:.2f}\n"
            print(f"Deposito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido!")
        

    elif opcao == "2":
        qtd_saque = qtd_saque + 1
        valor = float(input("Quanto voce quer sacar? "))

        if valor > 0:
            if valor <= saldo: 
                if qtd_saque < 3 and saldo < limite_saque:
                    saldo = saldo - valor
                    extrato = extrato + f"Saque: R$ {valor:.2f}\n"
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                else:
                    print("Limite de saldo ja foi atingido")
            else:
                print("Saldo insuficiente!")
        else:
            print("Valor inválido!")


    elif opcao == "3":
        print("Nao foram realizadas movimentaçoes" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "4":
        break

    else:
        print("Operaçao invalida")
        
    
   





