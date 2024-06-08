import textwrap

def menu():
    menu = """

    [d] Depositar   
    [s] Sacar
    [e] Extrato
    [nu] Novo usuario
    [nc] Nova conta
    [lc] Listar contas
    [q] Sair
    => """
    return input(textwrap.dedent(menu))


def criar_usuario(usuarios):
    cpf = input("Informe o seu cpf(apenas numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Ja existe usuario com esse cpf")
        return

    nome = input("Qual seu nome completo: ")
    data_nascimento = input("Qual sua data de nascimento(dd-mm-aaa): ")
    endereco = input("Qual seu endereço(logradourom, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario criado com sucesso!!")
    

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o seu cpf(apenas numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nusuario n encontrado, fluxo de criaçao de conta encerrado")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R${valor:.2f}\n"      
            
    else:
        print("valor invalido!")

    return saldo, extrato
    

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente")
    elif valor > limite:
        print("Passou do limite de valor")
    elif numero_saques > limite_saques:
        print("Passou do limite de saques")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("valor invalido!")

    return saldo, extrato


def extrato(saldo, /, *, extrato):
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(f"""{extrato}
---------------------------------------
        Saldo atual da conta: R${saldo:.2f}
""")


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Qual valor que voce quer depositar? "))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "s":        
            valor = float(input("Qual valor voce quer sacar? "))
            saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques)

        elif opcao == "e":
           extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
         break

        else:
            print("operação inválida, por favor selecione novamente a operação desejada")

main()






