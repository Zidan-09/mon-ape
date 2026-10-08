""" Converte o texto para minúsculas sem usar .lower():
    1. Percorro cada caractere de 'texto' com o for.
    2. Pego o código dele na tabela ASCII com ord():
       - 'A' a 'Z' vai de 65 a 90
       - 'a' a 'z' vai de 97 a 122
    3. Se o código está entre 65 e 90 (é maiúscula),
       somo 32 para cair no código da mesma letra minúscula.
       Ex: ord('B') = 66 -> 66 + 32 = 98 -> chr(98) = 'b'
    4. Converto de volta com chr() e imprimo sem pular linha.
"""
texto = input("Digite o texto: ")

for i in texto:
    code = ord(i)

    if 65 <= code <= 90:
        code += 32

    print(chr(code), end="")