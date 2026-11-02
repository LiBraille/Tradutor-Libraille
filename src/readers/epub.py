import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

def extrair_texto_epub(caminho_arquivo):
    # Abertura de epub
    livro = epub.read_epub(caminho_arquivo)
    print("Livro aberto com sucesso!")
    
    # Lista
    blocos_de_texto = []

    # Verifica cada documento capítulo/página arquivo
    for item in livro.get_items_of_type(ebooklib.ITEM_DOCUMENT): # O 'ITEM_DOCUMENT' é um filtro para ele ignorar capas e imagens
        conteudo_html = item.get_content()
        
        # Usa o beautifulsoup para limpar código
        sopa = BeautifulSoup(conteudo_html, 'html.parser')
        
        # Procura de conteúdo
        for elemento in sopa.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):
            texto = elemento.get_text(strip=True)
            
            if texto:
                # Define se é título ou parágrafo baseado na tag html
                if elemento.name.startswith('h'):
                    tipo_bloco = 'titulo'
                else:
                    tipo_bloco = 'paragrafo'
                    
                # Formato exigido pela arquitetura do projeto
                blocos_de_texto.append({"tipo": tipo_bloco, "texto": texto})
                
    return blocos_de_texto

# Teste exemplo
if __name__ == '__main__':
    arquivo_teste = "teste.epub"
    resultado = extrair_texto_epub(arquivo_teste)
    
    print(f"\nSucesso! Encontrei {len(resultado)} blocos de texto.")
    print("Primeiros 3 blocos extraídos:")
    for bloco in resultado[:3]:
        print(bloco)