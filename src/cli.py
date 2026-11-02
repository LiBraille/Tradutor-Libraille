import argparse
from readers.seletor import seletor

parser = argparse.ArgumentParser()

parser.add_argument("--arquivo", help="comando usado para fornecer o nome do arquivo.", type=str, required=True)
args = parser.parse_args()
resultado = seletor(args.arquivo)