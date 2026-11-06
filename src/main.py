from normalizador import normalizar_texto
from motor import carregar_tabela, traduzir_palavra
from codificador import converter_para_unicode, converter_para_binario
from readers.epub import extrair_epub
# Importando todos os motores

def executar():
    print("Tradutor Libraille iniciado!")
    caminho_livro = "teste.epub"
    caminho_tabela = "tables/ptbr/tabela.json"
    caminho_saida = "livro_traduzido.bin"
    # Pega configurações do livro de teste, tabela de tradução e saída

    regras = carregar_tabela(caminho_tabela)
    blocos = extrair_epub(caminho_livro)
    # Extrai todos os blocos de texto do livro

    numeros_totais = []

    # O for apenas calcula e guarda os números
    for posicao, bloco in enumerate(blocos):
        texto_original = bloco["texto"]
    # Pega todo o texto do bloco atual
    # E normaliza o texto

        if not texto_original.strip():
            continue
            # Pula blocos sem texto


    print(f'Processando bloco {posicao + 1}...')

    palavras_limpas = normalizar_texto(texto_original)

    for palavra in palavras_limpas:
        numeros = traduzir_palavra(palavra, regras)
        numeros_totais.extend(numeros)
        numeros_totais.append(0)
        # Adiciona um espaço em branco entre as palavras

    ver_resultado = converter_para_unicode(numeros_totais)

    print(f'Resultado: {ver_resultado}\n')

    converter_para_binario(numeros_totais, caminho_saida)
    print(f'Ficheiro {caminho_saida} criado com sucesso!\n')    
    print()

if __name__ == '__main__':
    executar()