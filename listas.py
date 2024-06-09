# lista pode ser criada com o construtor list ou colocando os valores entre []

frutas = ["laranja", "uva", "maca"]

frutas = []

letras = list("python") #[p, y, t, h, o, n]

numeros = list(range(10)) # 0 1 2 3 4 5 6 7 8 9

carro = ["ferrari", "f8", 4200000, 2020, 2900, "sp", True]


#acesso direto - acessar os dados usando o indice

frutas = ["laranja", "uva", "maca"]
frutas[0] #laranja
frutas[2] #maca
frutas[-1] #maca
frutas[-2] #uva


#lista aninhada - uma dentro da outra

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0] # [1, "a", 2] 
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"


#fatiamento - p extrair um conj de valores de uma seq

lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ["t", "h", "o", "n"]
lista[:2] # ["p", "y"]
lista[1:3] # ["y", "t"]
lista[0:3:2] # ["p", "t"]
lista[::] # ["p", "y", "t", "h", "o", "n"]
lista[::-1] # ["n", "o", "h", "t", "y", "p"]


#percorrer a lista - usa o for

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


#funçao enumerate - p saber o indice do objeto dentro do for

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):  #indice é o contador e o carro é o item
    print(f"{indice}: {carro}")


#compreensao de lista - criar lista a partir de uma q ja existe

    #filtro versao 1

    numeros = [1, 30, 21, 2, 9, 65, 34]
    pares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)

    #filtro versao 2 - com compreension

    numeros = [1, 30, 21, 2, 9, 65, 34] 
    pares = [numero for numero in numeros if numero % 2 == 0]


    #modificando valores versao 1
    numeros = [1, 30, 21, 2, 9, 65, 34]
    quadrado = []

    for numero in numeros:
        quadrado.append(numero ** 2)


    #modificando valores versao 2
    numeros = [1, 30, 21, 2, 9, 65, 34]
    quadrado = [numero ** 2 for numero in numeros]


#---------------------------------------------------------------------

#Metodos da lista

#[].append - para adicionar elemento na lista

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, "Python", [40, 30, 20]]




#[].clear - para limpar a lista

lista = [1, "Python", [40, 30, 20]]

print(lista) # [1, "Python", [40, 30, 20]]

lista.clear()

print(lista) # []




#[].copy - para retornar uma lista igual com outra instancia

lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista) # [1, "Python", [40, 30, 20]]

print(l2) # [1, "Python", [40, 30, 20]]




#[].count - para contar qntas vezes aparece o negocio na lista

cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1




#[].extend - para adicionar elementos (uma lista adicionada a outra)

linguagens = ["python", "js", "c"]

print(linguagens) # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens) # ["python", "js", "c", "java", "csharp"]




#[].index - para saber a primeira posiçao do objeto

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.index("java") # 3
linguagens.index("python") # 0




#[].pop - para adicionar itens da esq pra direita

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.pop() # csharp
linguagens.pop() # java
linguagens.pop() # c
linguagens.pop(0) # python

#[].remove - para remover itens pelo valor do item

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens) # ["python", "js", "java", "csharp"]


#[].reverse - reverter

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens) # ["csharp", "java", "c", "js", "python"]




#[].sort - para ordenar a lista 

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort() # ["c", "csharp", "java", "js", "python"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True) # ["python", "js", "java", "csharp", "c"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "c"]




#[].len - para mostrar o tamanho da lista

linguagens = ["python", "js", "c", "java", "csharp"]

len(linguagens) # 5




#[].sorted - para ordenar

linguagens = ["python", "js", "c", "java", "csharp"]

sorted(linguagens, key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]

sorted(linguagens, key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "c"] 