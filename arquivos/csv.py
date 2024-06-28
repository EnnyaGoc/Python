#armazena dados tabulares

#modulo csv para lidar cm arqs CSV

import csv

with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["nome", "idade"])
    writer.writerow(["ana", 30])
    writer.writerow(["joao", 25])


#------------------------------------------------------

import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

COLUNA_ID = 0
COLUNA_NOME = 1

try:
    with open(ROOT_PATH / "usuarios.csv", "w", newline='', encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome"])
        escritor.writerow(["1", "maria"])
        escritor.writerow(["2", "joao"])
except IOError as exc:
    print(f"erro ao criar o arq. {exc}")


try:
    with open(ROOT_PATH / "usuarios.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for idx, row in enumerate(leitor):
            if idx == 0:
                continue
            print(f"ID: {row[COLUNA_ID]}")
            print(f"Nome: {row[COLUNA_NOME]}")
except IOError as exc:
    print(f"erro ao criar o arq. {exc}")


try:
    with open(ROOT_PATH / "usuarios.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if idx == 0:
                print(f"ID: {row['id']}")
                print(f"Nome: {row['nome']}")
except IOError as exc:
    print(f"erro ao criar o arq. {exc}")

#Praticas recomendadas
#manipular os arqs com csv.reader e csv.writer
#tratar corretamente as exceçoes
#ao gravar aqrs csv, definir o argumento newline='' no metodo 'open'