from pathlib import Path
from .txt import ler_txt
from .epub import extrair_epub

# Abaixo, a extensão (suffix/sufixo) do arquivo recebe uma função expecifica que é seu reader correspondente.
sufixos = {".txt": ler_txt, ".epub": extrair_epub}

def seletor(arquivo):
    extensao = Path(arquivo).suffix.lower() # Pega a última extensão do arquivo, coloca para minusculo e retorna como uma string

    try:
        leitor = sufixos[extensao]
    except KeyError:
        raise ValueError(f"Formato não suportado: {extensao}") from None

    blocos = leitor(arquivo)

    return blocos
