#filenotfounderror - quando o arq n é encontrado

try:
    file = open('non_existent.file.txt', 'r')
except FileNotFoundError: #except FileNotFoundError as exc:
    print("arq n encontrado.")  
    #print(exc)
    #exc captura o detalhe do erro

#permissionerror - qndo tenta abrir um arq sem permissao
#ioerror - erro geral
#unicodedecodeerror - erro ao tentar decodificar os dados de um arq cm uma codificaçao inadequada
#unicodeencodeerror - erro ao tentar codificar os dados de um arq cm uma codificaçao inadequada


#isadirectoryerror - tentativa de abrir um diretorio em vez de um arq de texto

from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "novo-diretorio")
except IsADirectoryError as exc:
    print(f"nao foi possivel abrri o arq: {exc}")  
   
#pode colocar todas as tratativas em um unico bloco
except IOError as exc:
    print(f"erro ao abrir o arq: {exc}")  
except Exception as exc:
    print(f"algum problema ocorreu ao tentar abrir o arq: {exc}")  
#Se quiser deixar mais generico só colocar o Except