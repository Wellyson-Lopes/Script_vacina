import sqlite3
from sqlite3 import Error

#CONEXÃO COM BANCO DE DADOS
def conexaoBanco():
    caminho = "C:\\Users\\Wellyson Lopes\\Documents\\script_vacina\\Script_vacina\\banco_vacinas.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con
vcon = conexaoBanco()

#CRIAÇÃO DE TABELA
vsql="""CREATE TABLE tipo_vacinas(id INTEGER PRIMARY KEY AUTOINCREMENT, vacina VARCHAR(30), periodo INTEGER, dose INTEGER);"""

def criartabela(conexao,sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        print("Tabela Criada com Sucesso!")
    except Error as ex:
        print(ex)

criartabela(vcon,vsql)

vcon.close()