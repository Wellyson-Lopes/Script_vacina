import sqlite3
from sqlite3 import Error

#CONEXÃO COM BANCO DE DADOS
def conexaoBanco():
    caminho = "./banco_vacinas.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con
