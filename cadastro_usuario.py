from ast import Pass
from conexao_banco import *
import datetime
from datetime import timedelta, date
import schedule
import time

def consulta(conexao,sql):
    cursor = conexao.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchone()
    return resultado   

def allconsulta():
    consulta_tabela = vcon.cursor()
    consulta_tabela.execute(vsql)
    cst = consulta_tabela.fetchall()
    return cst

def inserir(conexao,cadastro):
    try:
        cursor = conexao.cursor()
        cursor.execute(cadastro)
        conexao.commit()
        print("Registro de tabela feito com Sucesso!!")
    except Error as ex:
        print(ex)

def allconsulta():
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


vsql = "SELECT * FROM usuarios"
res = consulta(vcon,vsql)
cst = allconsulta()

if res == None:
    usuario_resposavel = input("Não a Usuários cadastrdos em nosso banco de dados, por favor, escreva seu nome")
    filho = input(f"{usuario_resposavel}, insira o nome de seu filho(a): ")
    cadastro = "INSERT INTO usuarios (nome,filho) VALUES ('"+usuario_resposavel+"','"+filho+"')"
    inserir(vcon,cadastro)
else:
    print("estes são os usuarios cadastrados em nossa tabela")
    for i in (cst):
        print(f"Responsável: {i[1]}, filho(a): {i[2]} e o seu ID é {i[0]}: ")
    cadastrado = input("deseja se cadastrar? escreva: [S], ou deseja logar na sua conta escreva: [L]: ")
    if cadastrado == "S" or cadastrado == "s":
        usuario_resposavel = input("Por favor, escreva seu nome: ")
        filho = input(f"{usuario_resposavel}, insira o nome de seu filho(a): ")
        cadastro = "INSERT INTO usuarios (nome,filho) VALUES ('"+usuario_resposavel+"','"+filho+"')"
        inserir(vcon,cadastro)
        allconsulta()
        cst = allconsulta() 
        for i in (cst):
            print(f"Usuários cadastrados, Resposavel: {i[1]}, filho {i[2]} seu ID é {i[0]}: ")
        id_cadastrado = input("escreva o numero referente ao ID do seu cadastro: ")
        vsql = "SELECT * FROM usuarios WHERE id = '"+id_cadastrado+"'"
        cst = allconsulta()
        for r in cst:
            print(f"Olá {r[1]},  seja bem vindo ao nosso sistema!!!")
        usuario_resposavel = r[1]
        filho = r[2] 
        
    elif cadastrado == "L" or cadastrado == "l":
        id_cadastrado = input("escreva o numero referente ao ID do seu cadastro: ") 
        vsql = "SELECT * FROM usuarios WHERE id = '"+id_cadastrado+"'"
        cst = allconsulta()
        for r in cst:
            print(f"Olá {r[1]},  seja bem vindo ao nosso sistema!!!")
        usuario_resposavel = r[1]
        filho = r[2] 
    else:
        print("você digitou uma informação errada. Escreva novamente!!!")

consultar_vacina = input(f"{usuario_resposavel}, você deseja cadastrar uma nova vacina? se sim escreva: [CD] ou se deseja consultar tabela de vacinas escrva: [CS]: ")

if consultar_vacina == "CD" or consultar_vacina == "cd":
    tipo = input(f"""Olá {usuario_resposavel},  escreva o tipo de vacina que {filho} recebeu: 
[BCG], [HepatiteB], [TripliceBacteriana], [influenzaeb], [Poliomelite], 
[Pneumococicas], [Meningococicas], [MeningococicasB], 
[Febre_Amarela], [HepatiteA], [Triplice_viral], [Varicela]: """)

    dose = dose_vacina_inteiro("escreva a dose referente a esta vacina: ")
    dose = str(dose)

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
        mes = data_vacina_inteiro("Digite o mês da sua vacina: ")

    ano = None
    while ano == None:
        ano = data_vacina_inteiro("Digite o ano da sua vacina: ")

    data_vacina = str(datetime.date(ano, mes, dia))

    vsql = "SELECT * FROM tipo_vacinas WHERE vacina = '"+tipo+"'"
    cst = allconsulta()
    for r in cst:
        print(f"a Vacina selecionada foi {r[1]} e o periodo é de {r[2]} dias")
    tipo = r[1]
    periodo = r[2]

    cadastro = "INSERT INTO vacinas_aplicadas (usuario,filho,vacina,data,doses) VALUES ('"+usuario_resposavel+"','"+filho+"', '"+tipo+"', '"+data_vacina+"','"+dose+"')"
    inserir(vcon,cadastro)
else:
   Pass

vsql = "SELECT * FROM vacinas_aplicadas WHERE filho = '"+filho+"'"
allconsulta()
cst = allconsulta() 
print(f" Olá {usuario_resposavel}: ")
for e in (cst):
    print(f"{e[2]} tomou a vacina: {e[3]} e seu ID é {e[0]} a data de sua vacina foi {e[4]} e é a {e[5]}° dose: ")
