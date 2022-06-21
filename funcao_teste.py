def tipo_vacina(pergunta_tipo):
    vacina_select = input(pergunta_tipo)
    if vacina_select == "Penta" or vacina_select == "penta":
        vacina_selecionada = vacina_select

    else:
        vacina_select == "Rotavirus" or vacina_select == "rotavirus"
        vacina_selecionada = vacina_select
    return vacina_selecionada


def ciclo_vacina():
    ciclo = None
    if tipo_vacina == "Penta" or tipo_vacina == "penta":
        ciclo = 60
    else:
        tipo_vacina == "Rotarivus" or tipo_vacina == "rotavirus"
        ciclo = 70
    return ciclo


vacina = tipo_vacina("Selecione o tipo de Vacina")
ciclo = ciclo_vacina()
print(vacina)
print(ciclo)
