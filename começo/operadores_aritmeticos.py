# + - * / //

#modulo
print(10 % 3)

#exponenciaçao
print(2 ** 3)

produto_1 = 10
produto_2 = 20

print(produto_1 + produto_2 + 20)

# Operadores de comparação
# igualdade ==
# diferença !=
# > e >=
# < e <=

saldo = 200
saque = 200

print(saldo == saque)
print(saldo != saque)
print(saldo > saque)
print(saldo >= saque)

# Operadores de atribuição
saldo = 500
saldo += 200
saldo -= 200
saldo *= 200
saldo /= 200
saldo //= 200
saldo %= 200
saldo **= 200

limite = 100
# Operadores logicos
saldo >= saque and saque <= limite
   
saldo >= saque or saque <= limite

contatos_emergencia = []
not 1000 > 1500 #true

not contatos_emergencia #true
#lista vazia em python é falso

not "saque 1500" #false

not "" #true

# Operadores de identidade - p comparar se 2 objetos ocupam a mesma posiçao na memoria

curso = "Curso de python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso # True

curso is not nome_curso # false

saldo is limite # true


# Operadores de associaçao - p verificar se um obj ta presente numa sequencia

curso = "Curso de python"
frutas = ["laranja","uva","limao"]
saques = [1500, 100]

"python" in curso #true
"maça" not in frutas #true
200 in saques #false