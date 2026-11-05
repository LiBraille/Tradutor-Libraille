import re

def ler_txt(caminho):
    with open(caminho, encoding="UTF-8-sig") as arquivo:
        texto =  arquivo.read()

    def separar_blocos():
        blocos = re.findall(r'\S.*?(?=\s*\n\s*\n|\s*\Z)', texto, re.DOTALL)

        for bloco in blocos:
            ...
        return blocos
    
    return separar_blocos()