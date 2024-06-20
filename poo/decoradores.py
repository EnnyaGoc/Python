#funçoes podem ser passadas como argumentos

def mensagem(nome):
    print("executando mensagem")
    return f"oi {nome}"

def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"ola, tudo bem com vc {nome}?"

def executar(funcao, nome):
    print("executando executar")
    return funcao(nome)


print(executar(mensagem, "ana"))
print(executar(mensagem_longa, "ana"))




#Inner functions - funçoes internas, funçoes q sao definidas dentro de outras funçoes

def principal():
    print("executando a funçao principal")

    def funcao_interna():
        print("execuntancdo a funçao interna")

    def funcao_2():
        print("executando a funçao 2")

    funcao_interna()
    funcao_2()

principal()




#Vc tb pode usar funçoes como valores de retorno

def calculadora(operacao):
    def soma(a, b):
        return a + b
    
    def sub(a, b):
        return a - b
    
    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b
    

    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div
        
    
op = calculadora("+")
print(op(2, 2))
op = calculadora("-")
print(op(2, 2))
op = calculadora("*")
print(op(2, 2))
op = calculadora("/")
print(op(2, 2))




#Decorador simples - junçao dos 2

def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")

    return envelope


def ola_mundo():
    print("ola mundo!")


ola_mundo = meu_decorador(ola_mundo)
ola_mundo()


#usando o açucar sintatico

#@meu_decorador
#def ola_mundo():
    #print("ola mundo!")


#ola_mundo()