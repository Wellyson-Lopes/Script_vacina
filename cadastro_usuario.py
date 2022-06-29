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
    cadastrado = input("você já está cadastrado? se sim escreva[S], se não escreva [N]: ")
    if cadastrado == "N" or cadastrado == "n":
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
        usuario_resposavel = i[1]
        filho = i[2] 
        
    elif cadastrado == "S" or cadastrado == "s":
        id_cadastrado = input("escreva o numero referente ao ID do seu cadastro: ") 
        vsql = "SELECT * FROM usuarios WHERE id = '"+id_cadastrado+"'"
        cst = allconsulta()
        for r in cst:
            print(f"Olá {r[1]},  seja bem vindo ao nosso sistema!!!")
        usuario_resposavel = r[1]
        filho = r[2] 
    else:
        print("você digitou uma informação errada. Escreva novamente!!!")



tipo = input(f"Olá {usuario_resposavel},  escreva o tipo de vacina que {filho} recebeu: [BCG], [hepatiteB], [DTP],[tetravalente] ou [VOP]: ")


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
print(data_vacina)

vsql = "SELECT * FROM tipo_vacinas WHERE vacina = '"+tipo+"'"
cst = allconsulta()
for r in cst:
    print(f"a Vacina selecionada foi {r[1]} e o periodo é de {r[2]}")
tipo = r[1]
periodo = r[2]

cadastro = "INSERT INTO vacinas_aplicadas (usuario,vacina,data) VALUES ('"+filho+"','"+tipo+"','"+data_vacina+"')"
inserir(vcon,cadastro)
vsql = "SELECT * FROM vacinas_aplicadas WHERE vacina = '"+tipo+"'"
allconsulta()
cst = allconsulta() 
for e in (cst):
    print(f" {e[1]}, tomou a vacina: {e[2]} e seu ID é {e[0]}: ")
