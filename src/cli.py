import argparse
from readers.seletor import seletor

parser = argparse.ArgumentParser()

parser.add_argument("--arquivo", help="comando usado para fornecer o nome do arquivo.", type=str, required=True)

if __name__ == "__main__":
    args = parser.parse_args()
    blocos = seletor(args.arquivo)
    