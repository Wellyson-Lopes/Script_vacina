import sqlite3
from sqlite3 import Error

def conexaoBanco():
    caminho = "C:\\Users\\Wellyson Lopes\\Documents\\script_vacina\\Script_vacina\\banco_vacinas.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

