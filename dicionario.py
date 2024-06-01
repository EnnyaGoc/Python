#conj n ordenado de pares chave:valor e as chaves sao unicas
#usando {} ou dict()

pessoa = {"nome": "guilherme", "idade": 28}

pessoa = dict(nome= "guilherme", idade= 28)

pessoa["telefone"] = "333-1234" # {"nome": "guilherme", "idade": 28, "teleofone": "333-1234"}




#acessando os dados

dados = {"nome": "guilherme", "idade": 28, "teleofone": "333-1234"}

dados["nome"] # "guilherme"
dados["idade"] # 28
dados["telefone"] # "333-1234"

dados["nome"] = "maria"
dados["idade"] = 18
dados["telefone"] = "5453-7543"

dados # {"nome": "maria", "idade": 18, "teleofone": "5453-7543"}




#dicionarios aninhados

contatos = {
    "guilherme@gmail.com": {"nome": "guilherme", "telefone": "3533-1234"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "3537-1234"},
    "ana@gmail.com": {"nome": "ana", "telefone": "3563-1234"},
    "lucas@gmail.com": {"nome": "lucas", "telefone": "3583-1234"},
}

contatos["giovana@gmail.com"]["telefone"] # "3537-1234"




#for

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

# guilherme@gmail.com: {"nome": "guilherme", "telefone": "3533-1234"}
# giovana@gmail.com: {"nome": "giovana", "telefone": "3537-1234"}
# ana@gmail.com: {"nome": "ana", "telefone": "3563-1234"}
# lucas@gmail.com: {"nome": "lucas", "telefone": "3583-1234"}