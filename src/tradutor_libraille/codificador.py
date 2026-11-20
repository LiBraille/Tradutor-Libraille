from pathlib import Path


def converter_para_unicode(lista_de_numeros):
    texto_braille = ""

    for numero in lista_de_numeros:
        texto_pedido = chr(0x2800 + numero)
        texto_braille += texto_pedido

    return texto_braille


def gerar_bytes_binario(lista_numeros):
    return bytes(lista_numeros)


def converter_para_binario(lista_numeros, caminho_saida):
    caminho_saida = Path(caminho_saida).with_suffix(".bin")
    bytes_braille = gerar_bytes_binario(lista_numeros)

    with open(caminho_saida, "wb") as ficheiro_binario:
        ficheiro_binario.write(bytes_braille)

    return caminho_saida