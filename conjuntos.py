#criando sets - coleçao q n possui objetos repetidos
#usado p elimitar duplicaçoes de listas
#pode ser feito com set() ou {}

set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

set("abacaxi") # {"b", "a", "c", "x", "i"}

set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}




#acessando os dados - tem q converter para lista antes

numeros = {1, 2, 3, 2}

numeros = list(numeros)

numeros[0]


#for 

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)


#enumerate

carros = {"gol", "celta", "palio"}

for indice, carro in enumerate(carros):  #indice é o contador e o carro é o item
    print(f"{indice}: {carro}")

#-------------------------------------------------------------------------

#métodos do set

#{}.union

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) # {1, 2, 3, 4}



#{}.intersection

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersectionon(conjunto_b) # {2, 3}




#{}.difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}




#{}.symetric_difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b) # {1, 4}




#{}.issubset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

#todo a ta em b mas nem todo b ta em a
conjunto_a.issubset(conjunto_b) # true 

#todo b ta em a mas nem todo a ta em b
conjunto_b.issubset(conjunto_a) # false




#{}.issuperset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

#todo b ta em a mas nem todo a ta em b
conjunto_a.issuperset(conjunto_b) # false 

#todo a ta em b mas nem todo b ta em a
conjunto_b.issuperset(conjunto_a) # true




#{}.isdisjoint - conj q nao se tocam

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) # true 
conjunto_a.isdisjoint(conjunto_c) # false 




#{}.add

sorteio = {1, 23}

sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42}




#{}.clear

sorteio = {1, 23}

sorteio # {1, 23}
sorteio.clear()
sorteio # {}




#{}.copy

sorteio = {1, 23}

sorteio # {1, 23}
sorteio.copy()
sorteio # {1, 23}




#{}.discard

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.discard(1)
numeros.discard(45)
numeros # {2, 3, 4, 5, 6, 7, 8, 9, 0}




#{}.pop

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.pop() # 0
numeros.pop() # 1
numeros # {2, 3, 4, 5, 6, 7, 8, 9, 0}




#{}.remove

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.remove() # 0
numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9}




#{}.len

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

len(numeros) # 10




#{}.in

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

1 in numeros # true
10 in numeros # false

