from normalizador import normalizar_texto
from motor import carregar_tabela, traduzir_palavra
from codificador import converter_para_unicode, converter_para_binario
from readers.epub import extrair_epub
from readers.txt import extrair_txt
# Importando todos os motores

def executar(caminho, tabela, nome_saida):
    print("Tradutor Libraille iniciado!")
    caminho_livro = caminho
    caminho_tabela = tabela
    caminho_saida = nome_saida
    # Pega configurações do livro de teste, tabela de tradução e saída

    regras = carregar_tabela(caminho_tabela)
    blocos = extrair_epub(caminho_livro)
    # Extrai todos os blocos de texto do livro e regras de tradução

    numeros_totais = []
    # Lista para os números gerados pelo motor
    ultimo_texto = ""
    # Aqui será guardado o texto do último bloco e sua tradução
    ultimo_bloco = []
    # Lista para os números do último bloco

    # O for apenas calcula e guarda os números
    for posicao, bloco in enumerate(blocos):
        # Para cada posicao do livro, pega o texto do bloco atual
        texto_original = bloco["texto"]
        # Pega todo o texto do bloco atual

        if not texto_original.strip():
            continue
            # Pula blocos sem texto (vazio)

        ultimo_texto = texto_original

        palavras_limpas = normalizar_texto(texto_original)
        # E normaliza o texto

        bloco_atual = []
        for palavra in palavras_limpas:
            numeros = traduzir_palavra(palavra, regras)
            # Traduz a palavra usando a tabela de tradução
            bloco_atual.extend(numeros)
            bloco_atual.append(0)
            # Adiciona um espaço em branco entre as palavras

        numeros_totais.extend(bloco_atual)
        # .extend adiciona os números do bloco atual ao total do livro
        numeros_totais.append(0)
        # Adiciona um espaço em branco entre os blocos

        ultimo_bloco = bloco_atual

    resultado_ultimo_bloco = converter_para_unicode(ultimo_bloco)
    ver_resultado = converter_para_unicode(numeros_totais)
    # Vai ler o texto todo e mostrar a tradução completa
    # E mostrar somente o ultimo bloco do texto
    

    print(f'Total de blocos processados: {len(blocos)}\n')
    # Vai ler todos os blocos do livro e mostrar quantidade
    print(f'Texto Original (Último bloco): {ultimo_texto}\n')
    print(f'Tradução do último bloco em Braille: {resultado_ultimo_bloco}\n')
    print(f'Contagem total caracteres Braille do livro: {(len(ver_resultado))}\n')
    # Vai ler todos os caracteres do livro e mostrar quantidade
    print(f'Tradução completa do livro: {ver_resultado}\n')
    # Mostra a tradução completa do livro

    converter_para_binario(numeros_totais, caminho_saida)
    print(f'Ficheiro {caminho_saida} criado com sucesso!\n')    
    # Apresenta nome de arquivo carregado

if __name__ == '__main__':
    # Aqui o name e o main representa o nome do arquivo
    # Se for o nome do arquivo, ele vai executar a função executar
    executar()