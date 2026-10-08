""" Conta quantas palavras há no texto:
    1. Leio o texto com input.
    2. Quebro em lista com split(" ") (separa a cada espaço).
       Ex: "oi mundo teste" -> ["oi", "mundo", "teste"]
    3. Uso len() nessa lista para obter a quantidade de palavras.
    4. Imprimo o número diretamente.
"""
texto = input("Digite o texto: ")

palavras = texto.split(" ")

quantidade = len(palavras)

print(quantidade)

# print(len(input("Digite o texto: ").split(" ")))