import datetime
from datetime import timedelta, date
import schedule
import time

usuario = input("Digite o nome do usuario: ")

vacina = input(f"{usuario},  selecione o tip ode vacina,'Penta', 'Rotavirus': ")

if vacina == "Penta" or vacina == "penta":
    vacina = vacina
    periodo = 60

elif vacina == "Rotavirus" or vacina == "rotavirus":
    vacina = vacina
    periodo = 50
else:
    print("as informações digitadas são inválidas, por favor escreva 'Penta' ou 'Rotavirus': ")


def data_vacina_inteiro(pergunta):
    data_vacina = input(pergunta)
    if data_vacina.isdigit():
        data = data_vacina
        data = int(data)
    else:
        data = None
        print(f"{usuario}, vcoê digitou um valor iválido. Tente novamente!!!")
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

data_vacina1 = datetime.date(ano, mes, dia)

print(
    f"{usuario}, você selecionou a vacina {vacina}, a data de sua vacina foi {data_vacina1} e o ciclo é de {periodo} dias")
data_final = data_vacina1 + timedelta(days=periodo)

print(f"sua proxima vacina {vacina} será no dia: {data_final}")

hoje = datetime.date.today()
data_vacina_select = data_final - hoje



def reepetirTarefa():
    print(f"Faltam {data_vacina_select} para sua proxima Vacina, {vacina}")

schedule.every(10).seconds.do(reepetirTarefa)

while 1:
    schedule.run_pending()
    time.sleep(1)