import conexao_banco
from conexao_banco import *

#CRIAÇÃO DE TABELA
vsql="""CREATE TABLE IF NOT EXISTS tipo_vacinas(id INTEGER PRIMARY KEY AUTOINCREMENT, vacina VARCHAR(30), periodo INTEGER, dose INTEGER);"""

def criartabela(conexao,sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        print("Tabela Criada com Sucesso!")
    except Error as ex:
        print(ex)

criartabela(vcon,vsql)

vcon.close()