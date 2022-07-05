from ast import Pass
from conexao_banco import *
import datetime
from datetime import timedelta
from datetime import date
from datetime import datetime
import sched, time
from funcoes import *


vsql = "SELECT * FROM usuarios"
res = consulta(vcon,vsql)
cst = allconsulta(vsql)

while True:
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
            allconsulta(vsql)
            cst = allconsulta(vsql) 
            for i in (cst):
                print(f"Usuários cadastrados, Resposavel: {i[1]}, filho {i[2]} seu ID é {i[0]}: ")
            id_cadastrado = input("escreva o numero referente ao ID do seu cadastro: ")
            vsql = "SELECT * FROM usuarios WHERE id = '"+id_cadastrado+"'"
            cst = allconsulta(vsql)
            for r in cst:
                print(f"Olá {r[1]},  seja bem vindo ao nosso sistema!!!")
            usuario_resposavel = r[1]
            filho = r[2] 
            break
            
        elif cadastrado == "L" or cadastrado == "l":
            id_cadastrado = input("escreva o numero referente ao ID do seu cadastro: ") 
            vsql = "SELECT * FROM usuarios WHERE id = '"+id_cadastrado+"'"
            cst = allconsulta(vsql)
            for r in cst:
                print(f"Olá {r[1]},  seja bem vindo ao nosso sistema!!!")
            usuario_resposavel = r[1]
            filho = r[2]
            break
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

    dia = None
    while dia == None:
        dia = data_vacina_inteiro("Digite o dia o dia da sua vacina: ")

    mes = None
    while mes == None:
        mes = data_vacina_inteiro("Digite o mês da sua vacina: ")

    ano = None
    while ano == None:
        ano = data_vacina_inteiro("Digite o ano da sua vacina: ")

    data_vacina = date(ano,mes,dia)
    # a variavel periodo é representada em periodos de 30 dias * a quantidade de meses,
    #   depois deve ser convertida para meses ou anos
    vsql = "SELECT * FROM tipo_vacinas WHERE vacina = '"+tipo+"'"
    cst = allconsulta(vsql) 
    for r in (cst):
        periodo = 0
        if tipo == "BCG":
            periodo = r[2]
        elif tipo == "HepatiteB":
            periodo = r[2] * 2
        elif tipo == "TripliceBacteriana":
            periodo = r[2] * 2
        elif tipo == "influenzaeb":
            periodo = r[2] * 2
        elif tipo == "Poliomelite":
            periodo = r[2] * 2
        elif tipo == "Pneumococicas":
            periodo = r[2] * 2
        elif tipo == "Meningococicas":
            periodo = r[2] * 2
        elif tipo == "MeningococicasB":
            periodo = r[2] * 2
        elif tipo == "Febre_Amarela":
            periodo = r[2] * 36
        elif tipo == "HepatiteA":
            periodo = r[2] * 6
        elif tipo == "Triplice_viral":
            periodo = r[2] * 3
        elif tipo == "Varicela":
            periodo = r[2] * 3    

    vsql = "SELECT * FROM vacinas_aplicadas WHERE vacina = '"+tipo+"'"
    cst = allconsulta(vsql)
    for r in cst:
        print(f"a Vacina selecionada foi {r[3]} e o periodo é de {periodo} dias")
    tipo
    data_vacina = date(ano, mes, dia)
    data_vacina = str(data_vacina)
    periodo = str(periodo)
    usuario_resposavel = str(usuario_resposavel)
    filho = str(filho)
    tipo = str(tipo)

    cadastro = "INSERT INTO vacinas_aplicadas (usuario,filho,vacina,data,doses,periodo) VALUES ('"+usuario_resposavel+"','"+filho+"', '"+tipo+"', '"+data_vacina+"','"+dose+"','"+periodo+"')"
    inserir(vcon,cadastro)
else:
   Pass

vsql = "SELECT * FROM vacinas_aplicadas WHERE filho = '"+filho+"'"
cst = allconsulta(vsql) 
print(f" Olá {usuario_resposavel}: ")
for r in (cst):
    filho = r[2]
    tipo = r[3]
    id_cadastrado = r[0]
    data_vacina = r[4]
    dose = r[5]
    print(f"{filho} tomou a vacina: {tipo} o ID da vacina é {id_cadastrado} a data de sua vacina foi {data_vacina} e é a {dose}° dose: ")   
    
    tipo = r[3]
vsql = "SELECT * FROM vacinas_aplicadas WHERE filho = '"+filho+"'"
cst = allconsulta(vsql)
for r in (cst):
    periodo = r[6]  
    int(periodo)
    
vsql = "SELECT * FROM vacinas_aplicadas WHERE filho = '"+filho+"'"
cst = allconsulta(vsql)
for r in (cst):
    periodo = r[6]
    data_vacina = r[4]
    data_time = datetime.strptime(data_vacina, "%Y-%m-%d").date()
    data_final = data_time + timedelta(days=int(periodo))
    
    if periodo == 0:
        print(f"Parabéns ,{filho} está protegido com a vacina {tipo} !")
    else: 
        print(f"A proxima dose da vacina {tipo} será no dia: {data_final}")
        allconsulta(vsql)
        usuario_resposavel = r[1]
        tipo = r[3]
        hoje = date.today()
        data_vacina_select = data_final - hoje

if periodo != 0:
    schedule.every(10).seconds.do(reepetirTarefa,vsql, filho)
    contador = 0
    while contador <= 50:
        schedule.run_pending()
        time.sleep(1)
        contador += 1
else:
    print(f"{usuario_resposavel}, volte sempre !")