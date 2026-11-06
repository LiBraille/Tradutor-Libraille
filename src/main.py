from normalizador import normalizar_texto
from motor import carregar_tabela, traduzir_palavra
from codificador import converter_para_unicode, converter_para_binario
from readers.epub import extrair_epub
# Importando todos os motores

def executar():
    print("Tradutor Libraille iniciado!")
    caminho_livro = "teste.epub"
    caminho_tabela = "src/tables/ptbr/tabela.json"
    caminho_saida = "livro_traduzido.bin"

    regras = carregar_tabela(caminho_tabela)
    blocos = extrair_epub(caminho_livro)

    primeiro_bloco = blocos[0]
    texto_original = primeiro_bloco["texto"]

    print(f'Texto original: {texto_original}')
    print()

    palavras_limpas = normalizar_texto(texto_original)
    
    print(f'Palavras limpas: {palavras_limpas}')
    print()

    numeros_totais = []
    for palavra in palavras_limpas:
        numeros = traduzir_palavra(palavra, regras)
        numeros_totais.extend(numeros)
        numeros_totais.append(0)
       
