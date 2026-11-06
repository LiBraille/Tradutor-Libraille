import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup  # Usa o beautifulsoup para limpar código (html, xml e outros)

# Criando função de extração
def extrair_epub(caminho_arquivo):
    # Abertura de epub
    livro = epub.read_epub(caminho_arquivo)
    print("Livro aberto com sucesso!")
    
    # Lista para armazenar blocos de texto
    blocos_de_texto = []

    # Verifica cada documento capítulo/página arquivo
    for item in livro.get_items_of_type(ebooklib.ITEM_DOCUMENT): # O 'ITEM_DOCUMENT' é um filtro para ignorar capas e imagens
        # Processa somente o conteúdo do item
        conteudo_html = item.get_content() 
        # Retorna o conteúdo do item como bytes
        
        texto_limpo = BeautifulSoup(conteudo_html, 'html.parser')
        # A texto_limpo é uma variavel que guarda o texto limpo
        
        # Procura de conteúdo
        for elemento in texto_limpo.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):
            texto = elemento.get_text(strip=True)
            # (get_text() com strip=True é para remover espaços em branco e quebra de linha)
            
            if texto:
                # Define se é título ou parágrafo baseado na tag html
                if elemento.name.startswith('h'):
                    tipo_bloco = 'titulo'
                else:
                    tipo_bloco = 'paragrafo'
                    
                # Formato exigido pela arquitetura do projeto
                blocos_de_texto.append({"tipo": tipo_bloco, "texto": texto})
                # Adicionando conteúdo adquirido na lista
                
    return blocos_de_texto
