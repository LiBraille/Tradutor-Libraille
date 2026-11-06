from unicodedata import normalize

def normalizar_texto(texto):
    texto_nfc = normalize('NFC', texto)
    # Unifica acentuação em caracteres
    texto_sem_quebra = texto_nfc.replace('\n', ' ')
    # Remover espaços extras
    texto_limpo = ' '.join(texto_sem_quebra.split())
    # Separa o texto em palavras tirando espaços
    # Colar espaços entre palavras
    return texto_limpo

if __name__ == '__main__':
    texto_sujo = 'Este   é  um texto \n com  espaços estranhos e acentuação: maçã.'
    resultado = normalizar_texto(texto_sujo)
    print('Texto Original')
    print(texto_sujo)
    print('Texto Normalizado')
    print(resultado)
    print()