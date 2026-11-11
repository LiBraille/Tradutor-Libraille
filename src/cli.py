import argparse
from pathlib import Path
from main import executar


def main():
    parser = argparse.ArgumentParser(
        prog="libraille",
        description="Traduz arquivos de texto para braille, gerando um arquivo binário (.bin).",
    )

    parser.add_argument("-a", "--arquivo", help="Caminho do arquivo que será processado", type=Path, required=True)
    parser.add_argument("-t", "--tabela", help="Define a tabela que será usada", type=str, required=True)
    parser.add_argument("-s", "--saida", help="Define o nome do arquivo de saida", type=str, required=True)

    args = parser.parse_args()

    executar(
        caminho_livro=args.arquivo,
        tabela=args.tabela,
        caminho_saida=args.saida,
    )

if __name__ == "__main__":
    main()