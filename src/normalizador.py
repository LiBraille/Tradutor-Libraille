from unicodedata import normalize

def normalizar_texto(texto):
    texto_nfc = normalize('NFC', texto)
    # nfc é uma normalização que une caracteres com acentuação
    # Unifica acentuação em caracteres
    texto_sem_quebra = texto_nfc.replace('\n', ' ')
    # Remover espaços extras
    # texto_limpo = ' '.join(texto_sem_quebras.split())
    # Separa o texto em palavras tirando espaços
    # Colar espaços entre palavras
    tokens = texto_sem_quebra.split()
    # Separação de palavras em lista para melhor identificação no convertimento para o braile
    return tokens