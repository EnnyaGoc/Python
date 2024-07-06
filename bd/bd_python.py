#é necessario usar o driver especifico pra aquele sgbd

#Conectando com o bd sqLite

#import sqlite3
#conexao = sqlite3.connect("clientes.db")



import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite") #"meu_banco.db"

#cursor - obj pra executar comandos no bd
cursor = conexao.cursor()

def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER  PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    conexao.commit()

#inserindo dados
def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()

def excluir_registro(conexao, cursor, id):
    data = (id,) # tem q colocar uma virgula quando passar a tupla com um unico valor
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()   


#fazendo em massa

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?);", dados)
    conexao.commit()

dados = [
    ("gui", "gui@gmail.com"),
    ("julia", "julia@gmail.com"),
    ("leo", "leo@gmail.com"),
]

inserir_muitos(conexao, cursor, dados)



#fetchone - retorna só um registro

def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

#fetchall - retorna todos os registros

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")

cliente = recuperar_cliente(cursor, 1)
print(cliente)


clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)





#Usando o sqlite3.Row ou row_factory
#cursor.row_factory = sqlite3.Row
#cursor.execute("SELECT * FROM minha_tabela WHERE id = 1") 
#resultr = cursor.fetchone()
#print(dict(result))





#Se for concatenar no execute, reduz a segurança pois a pessoa pode ver todos os registros
#No terminal: 1 OR 1=1 

#Forma incorreta:
#cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")





#------------------------------------------------------------




