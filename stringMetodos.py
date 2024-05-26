#Maiuscula, minuscuta e title

curso = "pYtHon"

print(curso.upper()) #PYTHON

print(curso.lower()) #python

print(curso.title()) #Python


#Removendo espaço em branco

curso = "   Python  "

print(curso.sprit()) #"Python"

print(curso.lsprit()) #"Python "

print(curso.rsprit()) #"   Python"

#junçoes e centralizaçao

print(curso.center(10, "#")) #"##Python##"

print(".".join(curso)) #"P.y.t.h.o.n"


#--------------------------------------------------------------------

#Interpolaçao de variaveis


#Metodo format
nome = "ana"
idade = 25
profissao = "programadora"
linguagem = "python"

print("ola, me chamo {}. Tenho {} anos de idade, trabalho como {} e estou matriculada no curso de {}".format(nome, idade, profissao, linguagem))

print("ola, me chamo {3}. Tenho {2} anos de idade, trabalho como {1} e estou matriculada no curso de {0}".format(linguagem, profissao, idade, nome))

print("ola, me chamo {name}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}".format(name=nome, idade=idade, profissao=profissao, linguagem=linguagem))


pessoa = {"nome": "ana", "idade": 35, "profissao": "programadora", "linguagem": "python"}

print("ola, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}".format(**pessoa))


#Metodo f-string
print(f"ola, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}")

#formatando cm o f-string

PI = 3.14159

print(f"valor de pi: {PI:.2f}") #valor de pi: 3.14

print(f"valor de pi: {PI:10.2f}") #valor de pi:          3.14


#------------------------------------------------------
 
#Fatiamento de strings

nome = "guilherme arthur de carvalho"


nome[0] #g

nome[-1] #o

nome[:9] #guilherme

nome[10:] #arthur de carvalho

nome[10:16] #arthur

nome[10:16:2] #atu

nome[:] #guilherme arthur de carvalho

nome[::-1] #ohlavrac ed ruhtra emrehliug


#----------------------------------------------------------------

#Strings triplas

nome = "guilherme"

mensagem = f'''
    ola meu nome é {nome},
  eu estou aprendndo pyhton.
    essa msg tem diferentes recuos.
'''

#preserva os espaços
# ''' ou """

#   ola meu nome é {nome},
# eu estou aprendndo pyhton.
#   essa msg tem diferentes recuos. 



































