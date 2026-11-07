import re
from charset_normalizer import from_bytes

def ler_txt(caminho):
    with open(caminho, "rb") as arquivo:
        conteudo = arquivo.read()

    resultado = from_bytes(conteudo).best()

    if resultado is None:
        raise ValueError("Não foi possivel identificar a condificação do arquivo.")

    texto = str(resultado)

    return separar_blocos(texto)

def separar_blocos(texto):
    blocos = []
    lista_blocos = re.findall(r'\S.*?(?=\s*\n\s*\n|\s*\Z)', texto, re.DOTALL)

    for item in lista_blocos:
        dicionario = {"tipo": "paragrafo", "texto": item}
        blocos.append(dicionario)

    return blocos
