from sqlite3 import Error
import datetime
from datetime import timedelta
from datetime import date
from datetime import datetime
import schedule
import time
from conexao_banco import conexaoBanco

def consulta(conexao,sql):
    cursor = conexao.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchone()
    return resultado 

def allconsulta(vsql,vcon):
    consulta_tabela = vcon.cursor()
    consulta_tabela.execute(vsql)
    cst = consulta_tabela.fetchall()
    return cst

def inserir(conexao,cadastro):
    try:
        cursor = conexao.cursor()
        cursor.execute(cadastro)
        conexao.commit()
        print("Usuário cadastrado com Sucesso!!!")
    except Error as ex:
        print(ex)

def allconsulta(vsql):
    vcon = conexaoBanco()
    consulta_tabela = vcon.cursor()
    consulta_tabela.execute(vsql)
    cst = consulta_tabela.fetchall()
    return cst

def dose_vacina_inteiro(perguntadose):
    dose_vacina = input(perguntadose)
    if dose_vacina.isdigit():
        dose = dose_vacina
        dose = int(dose)
    else:
        dose = None
        print(f"{usuario_resposavel}, vcoê digitou um valor iválido. Tente novamente!!!")
    return dose

# input e comandos refentes as datas de vacinação
def data_vacina_inteiro(pergunta):
    data_vacina = input(pergunta)
    if data_vacina.isdigit():
        data = data_vacina
        data = int(data)
    else:
        data = None
        print(f"{usuario_resposavel}, vcoê digitou um valor iválido. Tente novamente!!!")
    return data

def reepetirTarefa(vsql, filho):
    vsql = "SELECT * FROM vacinas_aplicadas WHERE filho = '"+filho+"'"  
    cst = allconsulta(vsql)
    for r in (cst):
        data_vacina = r[4]
        periodo = r[6]
        int(periodo)
        data_time = datetime.strptime(data_vacina, "%Y-%m-%d").date()
        data_final = data_time + timedelta(days=periodo)
        hoje = date.today()
        data_vacina_select = data_final - hoje
        usuario_resposavel = r[1]
        filho= r[2]
        tipo = r[3]
        print(f"{usuario_resposavel} Faltam {data_vacina_select} para {filho} tomar sua proxima dose da Vacina, {tipo}")
