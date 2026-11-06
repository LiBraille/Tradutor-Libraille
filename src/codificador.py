def converter_para_unicode(lista_de_numeros):
    texto_braille = ''

    for numero in lista_de_numeros:
        texto_pedido = chr(0x2800 + numero)
        # O chr converte o número no seu desenho correspondente
        # 0x2800 é o primeiro símbolo em braille em branco (sem nenhum ponto)
        texto_braille += texto_pedido

    return texto_braille

# Motor binário
def converter_para_binario(lista_numeros, caminho_saida):
# Puxa a lista de números para um arquivo binário de saída
    bytes_braille = bytes(lista_numeros)
    # Converte a lista de números em bytes

    with open(caminho_saida, 'wb') as ficheiro_binario:
        ficheiro_binario.write(bytes_braille)


# Rodar teste visual
if __name__ == '__main__':
    numeros_teste = [17, 1, 47, 1]
    resultado = converter_para_unicode(numeros_teste)
    print()
    print(f'Números gerados pelo motor: {numeros_teste}')
    print(f'Resultado convertido para Unicode (Caracteres visuais): {resultado}')
    print(f'Número de caracteres convertidos: {len(resultado)}')
    # Mostrando a palavra 'caça'
    print()

# Rodar teste binário
nome_ficheiro = "teste.bin"
converter_para_binario(numeros_teste, nome_ficheiro)
print(f'Arquivo binário gerado: {nome_ficheiro}')
