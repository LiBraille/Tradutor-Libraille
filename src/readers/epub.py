import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

def extrair_texto_epub(caminho_arquivo):
    # O comando read_epub pega o arquivo e transforma num objeto que o Python entende
    livro = epub.read_epub(caminho_arquivo)
    print("Livro aberto com sucesso!")
    return livro

# Teste
if __name__ == '__main__':
    # Nome do arquivo de teste (substituir)
    arquivo_teste = "teste.epub"
    extrair_texto_epub(arquivo_teste)