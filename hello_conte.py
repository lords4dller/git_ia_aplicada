"""
Script simples de saudação personalizada.

Autor: Pietro Giacomin Conte
Curso: IA Aplicada - EsCom
"""


def saudacao(nome):
    """Retorna uma mensagem de saudação personalizada."""
    return f"Hello, {nome}!"


def main():
    nome = "Pietro Giacomin Conte"
    print(saudacao(nome))


if __name__ == "__main__":
    main()