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





#Vc tb pode usar funçoes como valores de retorno














# 