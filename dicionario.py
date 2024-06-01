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


#------------------------------------------------------------------------
#metodos

#{}.clear

contatos = {
    "guilherme@gmail.com": {"nome": "guilherme", "telefone": "3533-1234"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "3537-1234"},
    "ana@gmail.com": {"nome": "ana", "telefone": "3563-1234"},
    "lucas@gmail.com": {"nome": "lucas", "telefone": "3583-1234"},
}

contatos.clear()
contatos # {}




#{}.copy

contatos = {
    "guilherme@gmail.com": {"nome": "guilherme", "telefone": "3533-1234"}
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "gui"}

contatos["guilherme@gmail.com"] # {"nome": "guilherme", "telefone": "3533-1234"}
copia["guilherme@gmail.com"] # {"nome": "gui"}




#{}.fromkeys - cria chaves sem valor ou valor padrao

dict.fromkeys(["nome", "telefone"]) # {"nome": none, "telefone": none}

dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone": "vazio"}




#{}.get - acessando valores 

contatos = {
    "guilherme@gmail.com": {"nome": "guilherme", "telefone": "3533-1234"}
}

contatos["chave"] # keyerror

contatos.get("chave") # none
contatos.get("chave", {}) # {}
contatos.get("guilherme@gmail.com", {}) # {"guilherme@gmail.com": {"nome": "guilherme", "telefone": "3533-1234"}




#{}.items

contatos = {
    "guilherme@gmail.com": {"nome": "guilherme", "telefone": "3533-1234"}
}

contatos.items() # dict_items([("guilherme@gmail.com", {"nome": "guilherme", "telefone": "3533-1234"})])




#{}.keys - retorna só as chaves

contatos = {
    "guilherme@gmail.com": {"nome": "guilherme", "telefone": "3533-1234"}
}

contatos.keys() # dict_keys(["guilherme@gmail.com"])




#{}.pop - remove a chave e retorna o valor q removeu

contatos = {
    "guilherme@gmail.com": {"nome": "guilherme", "telefone": "3533-1234"}
}

contatos.pop("guilherme@gmail.com") # {"nome": "guilherme", "telefone": "3533-1234"}
contatos.pop("guilherme@gmail.com", {}) # {}




#{}.popitem - só remove

contatos = {
    "guilherme@gmail.com": {"nome": "guilherme", "telefone": "3533-1234"}
}

contatos.popitem() # ("guilherme@gmail.com", {"nome": "guilherme", "telefone": "3533-1234"})
contatos.popitem () # keyerror




#{}.setdefault - se o atributo n estiver no dicionario ele adiciona, se estiver ele retorna o valor e n altera

contato  = {"nome": "guilherme", "telefone": "3533-1234"}

contatos.setdefault("nome", "giovana") # "guilherme"
contato # {"nome": "guilherme", "telefone": "3533-1234"}

contatos.setdefault("idade", 28)
contato # {"nome": "guilherme", "telefone": "3533-1234", "idade": 28}




#{}.update - atualizar o dicionario com outro

contatos = {
    "guilherme@gmail.com": {"nome": "guilherme", "telefone": "3533-1234"}
}

contatos.update({"guilherme@gmail.com": {"nome": "gui"}})
contatos # {"guilherme@gmail.com": {"nome": "gui"}}

contatos.update({"giovana@gmail.com": {"nome": "giovana", "telefone": "3537-1234"}})
contatos # {"guilherme@gmail.com": {"nome": "gui"},"giovana@gmail.com": {"nome": "giovana", "telefone": "3537-1234"}}




#{}.values - retorna só os valores

contatos = {
    "guilherme@gmail.com": {"nome": "guilherme", "telefone": "3533-1234"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "3537-1234"},
    "ana@gmail.com": {"nome": "ana", "telefone": "3563-1234"},
    "lucas@gmail.com": {"nome": "lucas", "telefone": "3583-1234"},
}

contatos.values() # disct_values([{"nome": "guilherme", "telefone": "3533-1234"}, {"nome": "giovana", "telefone": "3537-1234"}, {"nome": "ana", "telefone": "3563-1234"}, {"nome": "lucas", "telefone": "3583-1234"}])




#{}.in - se algo é uma chave no dicionario

contatos = {
    "guilherme@gmail.com": {"nome": "guilherme", "telefone": "3533-1234"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "3537-1234"},
    "ana@gmail.com": {"nome": "ana", "telefone": "3563-1234"},
    "lucas@gmail.com": {"nome": "lucas", "telefone": "3583-1234"},
}

"guilherme@gmail.com" in contatos # true
"joao@gmail.com" in contatos # false
"idade" in contatos ["guilherme@gmail.com"] # false
"telefone" in contatos ["giovana@gmail.com"] # true




#{}.del - remover 

contatos = {
    "guilherme@gmail.com": {"nome": "guilherme", "telefone": "3533-1234"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "3537-1234"},
    "ana@gmail.com": {"nome": "ana", "telefone": "3563-1234"},
    "lucas@gmail.com": {"nome": "lucas", "telefone": "3583-1234"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["ana@gmail.com"]

contatos #{"guilherme@gmail.com": {"nome": "guilherme"},"giovana@gmail.com": {"nome": "giovana", "telefone": "3537-1234"}, "lucas@gmail.com": {"nome": "lucas", "telefone": "3583-1234"}}

