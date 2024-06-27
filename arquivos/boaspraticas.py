#bloco with garante o fechamento do bloco msm se um error ocorrer

from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "lorem.txt", "r") as arquivo:
        print(arquivo.read())

#verificar se o arq foi fechado com sucesso ou n
except IOError as exc:
    print(f"erro ao abrir o arq {exc}")


#use a codificaçao correta

try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("aprendendo a manipular arqs.")
except IOError as exc:
    print(f"erro ao abrir o arq {exc}")


try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"erro ao abrir o arq {exc}")
except UnicodeDecodeError as exc:
    print(exc)