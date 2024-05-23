nome = "julia"
idade = 30

nome = "ana"
print(nome, idade)

limite_saque_diario = 1000

STATES = ["RJ", "SP", "MG"]

STATES = 10

STATES = "RIO", "BRASILIA"

#convertendo valores

preco = 10
preco = float(preco) #10.0

#pode converter dividindo tb
preco = 10/2
print(preco) #5.5

preco = 10.3
preco = int(preco) #10

#--------------------

preco = 10
print(preco)

print(preco / 2) #5.0

print(preco // 2) #5

#--------------------

#Numero p string
preco = 10.5
idade = 28

print(str(preco)) #10.5
 #ou
texto = f"idade {idade} preco {preco}"
print(texto) #idade 28 preco 10.5

#string p numero
preco = "10.5"
idade = "28"

print(float(preco)) #10.5
print(int(idade)) #28



#NAO É POSSIVEL CONVERTER STRING(PALAVRA) P FLOAT

#para saber o tipo da variavel
type(preco)

#--------------------------------------------------
# Lendo valores cm o input
nome = input("informe seu nome:")


#exibindo valores cm print
nome = "gui"
sobrenome = "carvalho"

print(nome, sobrenome) # gui carvalho
print(nome, sobrenome, end="...\n") #g ui carvalho...
print(nome, sobrenome, sep="#") # gui#carvalho

