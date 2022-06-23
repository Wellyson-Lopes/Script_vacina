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
vcon = conexaoBanco()

def inserir(conexao,sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
        print("Registro de tabela feito com Sucesso!!")

    except Error as ex:
        print(ex)
continuar = "s"
while continuar == "s":
    tipo_vacina = input("adicione um tipo de vacina: ")
    periodo = input("adicione o clico em dias: ")
    dose = input("Adicione a quantidade de dose: ")
    vsql = "INSERT INTO tipo_vacinas (vacina,periodo,dose) VALUES ('"+tipo_vacina+"',"+periodo+","+dose+")"
    inserir(vcon,vsql)
    continuar = input("Deseja continuar? [s] para sim e [n] para não: ")
    if continuar == "s":
        continuar = "s"
    else:
        continuar = "n"

