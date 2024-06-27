#open() - para abrir o arq
#close() - p fechar

file = open("example.txt", "r")
#...
file.close()

#r para ler, w para gravar e a para colocar conteudo no arq q ja existe

file = open("example.txt", "r")
file = open("example.txt", "w")
file = open("example.txt", "a")



#-------------------------------------------------------------------------
#READ
#ler todo o conteudo do arq de uma vez
file = open("example.txt", "r")
print(file.read())
file.close()


#read retorna a string inteira do codigo

arquivo = open(
    "C:\Users\Marcia\Documents\repositorios-dos-outros\Python\arquivos\lorem.txt", "r"
)
print(arquivo.read())
file.close()



#readline retorna uma linha por vez

arquivo = open(
    "C:\Users\Marcia\Documents\repositorios-dos-outros\Python\arquivos\lorem.txt", "r"
)
print(arquivo.readLine())
file.close()


#readlines retorna uma lista de strings e tem todas as linhas do seu arq

arquivo = open(
    "C:\Users\Marcia\Documents\repositorios-dos-outros\Python\arquivos\lorem.txt", "r"
)
print(arquivo.readLines())
file.close()


#tip
# while len(linha := arquivo.readLine()):
#   print(linha)


#-------------------------------------------------------------------------
#WRITE
#sempre importante abrir do modo correto

file = open("example.txt", "r")
file.write("ola, mundo")
file.close()


#criando o arquivo
arquivo = open(
    "C:\Users\Marcia\Documents\repositorios-dos-outros\Python\arquivos/teste.txt", "w"
)
arquivo.write("escrevendo dados em um novo arquivo")

#writeLines escreve uma letra/palavra por vez
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])
arquivo.close()



#------------------------------------------------------------------------
#Gerenciando arquivos e diretórios

#da pra criar, renomear e excluir arqs e dirs usando os modulos 'os' e 'shutil'

import os
import shutil
from pathlib import Path

#pathlib serve pra vc pegar a pasta automaticamente, sem precisar escrever o caminho

ROOT_PATH = Path(__file__).parent

os.mkdir(ROOT_PATH / "novo-diretorio") #cria uma pasta na pasta pai

#criando arq
arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

#renomeando
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

#removendo
os.remove(ROOT_PATH / "alterado.txt")

#movendo de um diretorio p outro
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")