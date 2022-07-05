from ast import Pass, While
from cmd import PROMPT
from getpass import getpass
from conexao_banco import *
import datetime
from datetime import timedelta
from datetime import date
from datetime import datetime
import sched, time
from funcoes import *
import stdiomask


def menu():
    print("""           V.V.C Virtual Vaccine Card
            Sistema de Cadastro/Login          
Escolha uma Opção:
[1]Cadastrar novo usuário
[2]Login
[3]sair     
""")
    resposta = input("Digite uma opção [1] [2] ou [3]: ")
    if resposta.isdigit() and resposta == "1" or resposta == "2" or resposta == "3":
        opcao = resposta
        opcao = int(opcao)
    else:
        opcao = None
        print("Vcoê digitou um valor iválido. \n Tente novamente!!!")
        
    return opcao

def cadastro_user():
    usuario = input("Nome: ")
    login = input("E-mail: ")
    sexo = input("""             Escolha uma Opção           
[1]Masculino
[2]Feminino
    """)   
    while sexo != "1" and sexo != "2":
        sexo = input("""             Escolha uma Opção           
[1]Masculino
[2]Feminino
    """)
    senha = stdiomask.getpass(prompt="Senha: ", mask='*')
    if sexo == "1":
        sexo = "Masculino"
    else:
        sexo == "2"
        sexo = "Feminino"
    return(usuario, login, sexo, senha)

def consulta_user(login):
    try:
        vsql = "SELECT * FROM usuarios"
        consulta = allconsulta(vsql)
        for i in (consulta):
            email = i[2]
            if login == email:
                return True
    except FileNotFoundError:
        return False

def consulta_login(login, senha):
    try:
        vsql = "SELECT * FROM usuarios"
        consulta = allconsulta(vsql)
        for i in (consulta):
            email = i[2]
            password = i[3]
            if login == email and senha == password:
                return True
    except FileNotFoundError:
        return False


def login_user():
    login = input("E-mail: ")  
    senha = stdiomask.getpass(prompt="Senha: ", mask='*')
    return(login, senha)

opcao = None
while opcao == None:
    opcao = menu()


if opcao == 1:
    usuario, login, sexo, senha = cadastro_user()
    if usuario == senha:
        print("A senha não pode ser seu Nome! \nEscolha outra senha: ")
        senha = stdiomask.getpass(prompt="Senha: ",mask='*')
    user = consulta_user(login)
    if user == True:
        print("Este email já está cadastrado em nosso sistema! \nPor favor digite outro email:")
        cadastro_user()
        vsql = "SELECT * FROM usuarios"
        cadastro = f"INSERT INTO usuarios (usuario, email, senha, sexo) VALUES ('{usuario}', '{login}', '{senha}', '{sexo}')"
        inserir(vcon, cadastro)
        
    else:
        vsql = "SELECT * FROM usuarios"
        cadastro = "INSERT INTO usuarios (usuario, email, senha, sexo) VALUES ('"+usuario+"', '"+login+"', '"+senha+"', '"+sexo+"')"
        inserir(vcon, cadastro)


if opcao == 2:
        login, senha = login_user()
        user_busca = consulta_login(login,senha)
        if user_busca == True:
            vsql = "SELECT * FROM usuarios WHERE email = '"+login+"' "
            consulta = allconsulta(vsql)
            for i in (consulta):
                usuario = i[1]
                email = i[2]
                senha = i[3]
                sexo = i[4]
            print(f"Olá {usuario}, seja bem vindo ao nosso sistema!")
