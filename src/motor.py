import json 
# biblioteca que permite ler arquivos json e converter em string

def carregar_tabela(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as ficheiro:
    # with open abre o ficheiro e garante fechamento
    # encoding='utf-8' para ler caracteres (como acentuação)
        tabela = json.load(ficheiro)

    return tabela

def pontos_para_numero(pontos):
    if pontos == ['?']:
        # Se letra for desconhecida, retorna 0
        return 0

    # (Bitmasking) representa números binários para cada letra, responsavel pela representação em braille
    numero_braille = 0
    for ponto in pontos:
        valor = 2 ** (ponto - 1)
        # Converte ponto em número binário
        numero_braille += valor
        # Adiciona valor do ponto ao número braille

    return numero_braille

def traduzir_palavra(palavra, tabela):
    celulas_braille = []
    anterior = ""

    sinal_maiuscula = pontos_para_numero(tabela['regras']['maiuscula'])
    sinal_numero = pontos_para_numero(tabela['regras']['numero'])
    
    # Palavra inteira em maiúscula
    if palavra.isupper() and any(letra.isalpha() for letra in palavra):
        celulas_braille.extend([sinal_maiuscula] * 2)

    for letra in palavra:
        if letra in tabela['caracteres']:

            if letra.isupper() and palavra.isupper():
                pontos = tabela['caracteres'][letra]

            elif letra.isupper():
                celulas_braille.append(sinal_maiuscula)
                pontos = tabela['caracteres'][letra]

            elif letra.isdigit() and not anterior.isdigit():
                celulas_braille.append(sinal_numero)
                pontos = tabela['caracteres'][letra]

            else:
                pontos = tabela['caracteres'][letra]
            
            numero = pontos_para_numero(pontos)
            celulas_braille.append(numero)
            anterior = letra

        else:
            celulas_braille.append(0)
            anterior = letra

    return celulas_braille