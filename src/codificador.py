def converter_para_unicode(lista_de_numeros):
    texto_braille = ''

    for numero in lista_de_numeros:
        texto_pedido = chr(0x2800 + numero)
        # O chr converte o número no seu desenho correspondente
        # 0x2800 é o primeiro símbolo em braille em branco (sem nenhum ponto)
        texto_braille += texto_pedido

    return texto_braille

# Rodar teste
if __name__ == '__main__':
    numeros_teste = [17, 1, 47, 1]
    resultado = converter_para_unicode(numeros_teste)
    print()
    print(f'Números gerados pelo motor: {numeros_teste}')
    print(f'Resultado convertido para Unicode (Caracteres visuais): {resultado}')
    print(f'Número de caracteres convertidos: {len(resultado)}')
    # Mostrando a palavra 'caça'
    print()