# def palavra reservada para funçao

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}")

def exibir_mensagem_3(nome="gui"):
    print(f"seja bem vindo do {nome}")

exibir_mensagem()
exibir_mensagem_2(nome="gui")
exibir_mensagem_3()
exibir_mensagem_3(nome="ana")




# em py, a funçao pode retornar mais de um valor

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def func_3():
    print("ola mundo!")

calcular_total([10, 20, 34])    # 64
retorna_antecessor_e_sucessor(10) # (9, 11)
print(func_3()) # none




# argumentos noemados - q vai passar chave, valor

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("fiat", "palio", 1999, "abc-1234")
salvar_carro(marca="fiat", modelo="palio", ano=1999, placa="abc-1234")
salvar_carro(**{"marca": "fiat", "modelo": "palio", "ano": 1999, "placa": "abc-1234"})

# carro inserido com sucesso! fiat/palio/1999/abc-1234




# args e kwargs -> *args e **kwargs
# args os valores virao numa tupla, e kwargs num dicionario

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("sexta feira, 16 de ago de 2022","zen of python", "beautiful is better than ugly", autor="tim peters", ano=1999)

# ele sabe q é uma tupla poisé fornecido por ,
# sabe q é kwargs pois é chave valor