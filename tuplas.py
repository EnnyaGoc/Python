# estrutura de dados q parece a lista mas é mais restrita, imutável.
# usa a classe tuple ou os valores entre ()
# coloca , no final pro python saber q é uma tupla


frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)


#acesso direto - acessar os dados usando o indice

frutas = ("maçã", "laranja", "pera", "uva",)
frutas[0] #maca
frutas[2] #uva
frutas[-1] #pera
frutas[-3] #laranja



#tupla aninhada - uma dentro da outra

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)

matriz[0] # [1, "a", 2] 
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"




#fatiamento - p extrair um conj de valores de uma seq

lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ("t", "h", "o", "n")
lista[:2] # ("p", "y")
lista[1:3] # ("y", "t")
lista[0:3:2] # ("p", "t")
lista[::] # ("p", "y", "t", "h", "o", "n")
lista[::-1] # ("n", "o", "h", "t", "y", "p")




#percorrer a tupla - usa o for

carros = ("gol", "celta", "palio")

for carro in carros:
    print(carro)



#funçao enumerate - p saber o indice do objeto dentro do for

carros = ("gol", "celta", "palio")

for indice, carro in enumerate(carros):  #indice é o contador e o carro é o item
    print(f"{indice}: {carro}")



#----------------------------------------
#metodos

#[].count - para contar qntas vezes aparece o negocio na tupla

cores = ("vermelho", "azul", "verde", "azul")

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1




#[].index - para saber a primeira posiçao do objeto

linguagens = ("python", "js", "c", "java", "csharp")

linguagens.index("java") # 3
linguagens.index("python") # 0




#[].len - para mostrar o tamanho da tupla

linguagens = ("python", "js", "c", "java", "csharp")

len(linguagens) # 5