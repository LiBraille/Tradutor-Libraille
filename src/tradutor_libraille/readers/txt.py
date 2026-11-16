import re

def extrair_txt(caminho):
    with open(caminho, encoding="utf-8-sig") as arquivo:
        texto = arquivo.read()

    return separar_blocos(texto)

def separar_blocos(texto):
    blocos = []
    lista_blocos = re.findall(r'\S.*?(?=\s*(?:\r?\n\s*){2,}|\s*\Z)', texto, re.DOTALL)

    for item in lista_blocos:
        dicionario = {"tipo": "paragrafo", "texto": item}
        blocos.append(dicionario)

    return blocos
