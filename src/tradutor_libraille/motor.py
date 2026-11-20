import json
from importlib.resources import files


def carregar_tabela(tabela_nome="ptbr"):
    caminho = files("tradutor_libraille").joinpath("tables", f"{tabela_nome}.json")

    with caminho.open("r", encoding="utf-8") as ficheiro:
        tabela = json.load(ficheiro)

    return tabela


def pontos_para_numero(pontos):
    if pontos == ["?"]:
        return 0

    numero_braille = 0
    for ponto in pontos:
        valor = 2 ** (ponto - 1)
        numero_braille += valor

    return numero_braille


def traduzir_palavra(palavra, tabela):
    celulas_braille = []
    anterior = ""

    sinal_maiuscula = pontos_para_numero(tabela["regras"]["maiuscula"])
    sinal_numero = pontos_para_numero(tabela["regras"]["numero"])

    if palavra.isupper() and any(letra.isalpha() for letra in palavra):
        celulas_braille.extend([sinal_maiuscula] * 2)

    for letra in palavra:
        if letra in tabela["caracteres"]:
            if letra.isupper() and palavra.isupper():
                pontos = tabela["caracteres"][letra]
            elif letra.isupper():
                celulas_braille.append(sinal_maiuscula)
                pontos = tabela["caracteres"][letra]
            elif letra.isdigit() and not anterior.isdigit():
                celulas_braille.append(sinal_numero)
                pontos = tabela["caracteres"][letra]
            else:
                pontos = tabela["caracteres"][letra]

            numero = pontos_para_numero(pontos)
            celulas_braille.append(numero)
            anterior = letra
        else:
            celulas_braille.append(0)
            anterior = letra

    return celulas_braille