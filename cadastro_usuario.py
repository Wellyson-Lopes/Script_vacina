import conexao_banco
from conexao_banco import *

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
        print(f"Responsável: {i[1]}, filho(a): {i[2]} e o seu ID é {i[0]}")
    cadastrado = input("você já está cadastrado? se sim escreva[S], se não escreva [N]: ")
    if cadastrado == "N" or cadastrado == "n":
        usuario_resposavel = input("Por favor, escreva seu nome: ")
        filho = input(f"{usuario_resposavel}, insira o nome de seu filho(a): ")
        cadastro = "INSERT INTO usuarios (nome,filho) VALUES ('"+usuario_resposavel+"','"+filho+"')"
        inserir(vcon,cadastro)
        allconsulta()
        cst = allconsulta()  
        
    elif cadastrado == "S" or cadastrado == "s":
        id_cadastrado = input("escreva o numero referente ao ID do seu cadastro: ")
    else:
        print("você digitou uma informação errada. Escreva novamente!!!")

