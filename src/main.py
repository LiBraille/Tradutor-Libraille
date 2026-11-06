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

    primeiro_bloco = blocos[0]
    texto_original = primeiro_bloco["texto"]
    # Pega o texto do primeiro bloco do livro
    # E normaliza o texto

    print(f'Texto original: {texto_original}\n')

    palavras_limpas = normalizar_texto(texto_original)

    
    print(f'Palavras limpas: {palavras_limpas}\n')

    numeros_totais = []
    
    # Este 'for' apenas calcula e guarda os números
    for palavra in palavras_limpas:
        numeros = traduzir_palavra(palavra, regras)
        numeros_totais.extend(numeros)
        numeros_totais.append(0)

    # RECUAMOS para a esquerda: Isto só acontece DEPOIS de o 'for' terminar todas as palavras
    ver_resultado = converter_para_unicode(numeros_totais)
    print(f'Resultado: {ver_resultado}\n')

    converter_para_binario(numeros_totais, caminho_saida)
    print(f'Ficheiro {caminho_saida} criado com sucesso!\n')


# RECUAMOS para a margem esquerda: Fora da função 'executar'
if __name__ == '__main__':
    executar()