import conexao_banco
from conexao_banco import *

#CRIAÇÃO DE TABELA
vsql="CREATE TABLE IF NOT EXISTS tipo_vacinas(id INTEGER PRIMARY KEY AUTOINCREMENT, vacina VARCHAR(30), periodo INTEGER, dose INTEGER);"

def criartabela(conexao,sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        print("Tabela Criada com Sucesso!")
    except Error as ex:
        print(ex)

criartabela(vcon,vsql)


vsql="CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(30), filho VARCHAR(30));"

def criartabela(conexao,sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        print("Tabela Criada com Sucesso!")
    except Error as ex:
        print(ex)

criartabela(vcon,vsql)


vsql="CREATE TABLE IF NOT EXISTS vacina_aplicad(id INTEGER PRIMARY KEY AUTOINCREMENT, usuario INTEGER, vacina INTEGER, data TEXT);"

def criartabela(conexao,sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        print("Tabela Criada com Sucesso!")
    except Error as ex:
        print(ex)

criartabela(vcon,vsql)

vcon.close()