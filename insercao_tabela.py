from conexao_banco import *

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
    if continuar == "s" or continuar == "S":
        continuar = "s"
    else:
        continuar = "n"

