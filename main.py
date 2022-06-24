import datetime
from datetime import timedelta, date
import schedule
import time
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
#input de dados pessoais

usuario_resposavel = input("Escreva o seu nome: ")
filho = input(f"Olá {usuario_resposavel} tudo bem?, Escreva o nome de seu Filho(a)")
sexo = input(f"{usuario_resposavel} você é o Pai ou a mãe de {filho}, escreva [P] para Pai ou [M] para Mãe: ")
if sexo == "P" or sexo == "p":
    sexo = "Papai"
else:
    sexo = "Mamãe"

tipo = input(f"Olá {sexo} {usuario_resposavel},  escreva o tipo de vacina que {filho} recebu,[BCG], [hepatiteB], [DTP],[tetravalente] ou [VOP]: ")


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


dia = None
while dia == None:
    dia = data_vacina_inteiro("Digite o dia o dia da sua vacina: ")

mes = None
while mes == None:
    mes = data_vacina_inteiro("Digite o mês da sua vacina:")

ano = None
while ano == None:
    ano = data_vacina_inteiro("Digite o ano da sua vacina: ")

data_vacina = datetime.date(ano, mes, dia)



#conulta de dados para colocar dentro de variaveis com tuplas
def consulta(conexao,sql):
    cursor = conexao.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    return resultado

vsql = "SELECT * FROM tipo_vacinas WHERE vacina = '"+tipo+"'"
res = consulta(vcon,vsql)
for r in res:
    print(f"{sexo} {usuario_resposavel}, {filho} tomou a vacina {tipo}")

#esta condição está associada ao input do tipo da vacina na linha 28
periodo = 0
if tipo == "BCG":
    periodo = r[2]
elif tipo == "hepatiteB":
    periodo = r[2] * 2
elif tipo == "DTP":
    periodo = 0
elif tipo == "tetravalente":
    periodo = r[2] * 2
elif tipo == "VOP":
    periodo = r[2] * 2
periodo = int(periodo)

if periodo == 0:
    print(f"{sexo} {usuario_resposavel}, Está é uma Vacina de dose única !")
else:    
    print(f"{sexo} {usuario_resposavel}, a data da vacina de {filho} foi {data_vacina} e o ciclo é de {periodo} dias")

data_final = data_vacina + timedelta(days=periodo)
if periodo == 0:
    print(f"Parabéns {sexo} ,{filho} está protegido com a vacina {tipo} !")
else: 
    print(f"A proxima dose da vacina {tipo} será no dia: {data_final}")

hoje = datetime.date.today()
data_vacina_select = data_final - hoje



def reepetirTarefa():  
        print(f"{sexo} {usuario_resposavel} Faltam {data_vacina_select} para {filho} tomar sua proxima dose da Vacina, {tipo}")

if periodo != 0:
    schedule.every(10).seconds.do(reepetirTarefa)
    contador = 0
    while contador <= 50:
        schedule.run_pending()
        time.sleep(1)
        contador += 1
else:
    print(f"{usuario_resposavel}, volte sempre !")
