def ler_txt(caminho):
    with open(caminho, encoding="UTF-8") as arquivo:
        texto =  arquivo.read()

    blocos = separar_blocos(texto)
    for bloco in blocos:
        print(repr(bloco))
        #print(f"Bloco: {repr(bloco)}")

def separar_blocos(texto):
    def remover_brancas():
        nonlocal texto
        texto = texto.strip()

    remover_brancas()
    return texto.split('\n\n')
