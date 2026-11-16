from .normalizador import normalizar_texto
from .motor import carregar_tabela, traduzir_palavra
from .codificador import converter_para_unicode, gerar_bytes_binario, converter_para_binario
from .readers.seletor import seletor


def traduzir_arquivo(caminho_livro, tabela="ptbr"):
    regras = carregar_tabela(tabela)
    blocos = seletor(caminho_livro)

    numeros_totais = []
    ultimo_texto = ""
    ultimo_bloco = []

    for bloco in blocos:
        texto_original = bloco["texto"]

        if not texto_original.strip():
            continue

        ultimo_texto = texto_original
        palavras_limpas = normalizar_texto(texto_original)

        bloco_atual = []
        for palavra in palavras_limpas:
            numeros = traduzir_palavra(palavra, regras)
            bloco_atual.extend(numeros)
            bloco_atual.append(0)

        numeros_totais.extend(bloco_atual)
        numeros_totais.append(0)

        ultimo_bloco = bloco_atual

    resultado_ultimo_bloco = converter_para_unicode(ultimo_bloco)
    ver_resultado = converter_para_unicode(numeros_totais)
    bytes_binario = gerar_bytes_binario(numeros_totais)

    return {
        "bytes_binario": bytes_binario,
        "texto_braille": ver_resultado,
        "ultimo_bloco_braille": resultado_ultimo_bloco,
        "ultimo_texto_original": ultimo_texto,
        "total_blocos": len(blocos),
        "total_caracteres_braille": len(ver_resultado),
    }


def executar(caminho_livro, tabela, caminho_saida):
    print("Tradutor Libraille iniciado!")

    resultado = traduzir_arquivo(caminho_livro=caminho_livro, tabela=tabela)

    print(f"Total de blocos processados: {resultado['total_blocos']}\n")
    print(f"Texto Original (Último bloco): {resultado['ultimo_texto_original']}\n")
    print(f"Tradução do último bloco em Braille: {resultado['ultimo_bloco_braille']}\n")
    print(f"Contagem total caracteres Braille do livro: {resultado['total_caracteres_braille']}\n")
    print(f"Tradução completa do livro: {resultado['texto_braille']}\n")

    arquivo_gerado = converter_para_binario(list(resultado["bytes_binario"]), caminho_saida)
    print(f"Ficheiro {arquivo_gerado} criado com sucesso!\n")