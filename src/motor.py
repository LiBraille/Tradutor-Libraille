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
        # Se letra for desconhida, retorna 0
        return 0

    # (Bitmasking)
    numero_braille = 0
    for ponto in pontos:
        valor = (ponto - 1) ** 2 
        # Converte ponto em número binário
        numero_braille += valor

    return numero_braille

def traduzir_palavra(palavra, tabela):
    celulas_braille = []
    # Lista para armazenar pontos em braile

    for letra in palavra:
        letra = letra.lower()
        # Padroniza letras para minusculas, facilitar leitura de json

        if letra in tabela['caracteres']:
        # Se letra existe na tabela, converte em número braille
            pontos = tabela['caracteres'][letra]
            # Obtém pontos em braille correspondentes à letra
            numero = pontos_para_numero(pontos)
            # Identifica se letra existe no dicionário json
            celulas_braille.append(numero)
            

        else:
            celulas_braille.append(0)
            # Caso não exista na tabela, recebe 0

    return celulas_braille

# Rodar teste
if __name__ == '__main__':
    caminho_tabela = "tables/ptbr/tabela.json"
    regras = carregar_tabela(caminho_tabela)
    
    print('Tabela carregada com sucesso!')

    # Palavra teste
    palavra_teste = "caça"
    resultado = traduzir_palavra(palavra_teste, regras)
    print(f'\nA tradução da palavra "{palavra_teste}" em pontos em Braile é:')
    print(resultado)
