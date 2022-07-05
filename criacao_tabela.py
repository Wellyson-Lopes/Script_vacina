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


vsql="CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, usuario TEXT,  email TEXT, senha TEXT, sexo TEXT);"

def criartabela(conexao,sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        print("Tabela Criada com Sucesso!")
    except Error as ex:
        print(ex)

criartabela(vcon,vsql)


vsql="CREATE TABLE IF NOT EXISTS vacinas_aplicadas(id INTEGER PRIMARY KEY AUTOINCREMENT, usuario TEXT, filho TEXT, vacina TEXT, data DATETIME, doses INTEGER, periodo INTEGER, email TEXT, sexo_filho TEXT);"

def criartabela(conexao,sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        print("Tabela Criada com Sucesso!")
    except Error as ex:
        print(ex)

criartabela(vcon,vsql)

vsql="CREATE TABLE IF NOT EXISTS filhos (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, usuario TEXT, sexo_usuario TEXT, filho TEXT, sexo_filho TEXT,data_nascimento DATETIME);"

def criartabela(conexao,sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        print("Tabela Criada com Sucesso!")
    except Error as ex:
        print(ex)

criartabela(vcon,vsql)

vcon.close()
