from pathlib import Path

def converter_para_unicode(lista_de_numeros):
    texto_braille = ''
    # Armazena o texto braille convertido

    for numero in lista_de_numeros:
        texto_pedido = chr(0x2800 + numero)
        # O chr converte o número no seu desenho correspondente
        # 0x2800 é o primeiro símbolo em braille em branco (sem nenhum ponto)
        texto_braille += texto_pedido
        # Conta cada caractere convertido e adiciona ao texto braille

    return texto_braille

# Motor binário
def converter_para_binario(lista_numeros, caminho_saida):
    # Adiciona ou altera o sufixo para .bin
    caminho_saida = Path(caminho_saida).with_suffix(".bin")

    # Função para converter uma lista de números em um arquivo binário de saída
    bytes_braille = bytes(lista_numeros)
    # Converte a lista de números em bytes

    with open(caminho_saida, 'wb') as ficheiro_binario:
        ficheiro_binario.write(bytes_braille)
    # Aqui vai abrir o arquivo binário de saída e escrever os bytes
    # 'wb' significa escrever em modo binário
