""" Converte o texto para MAIÚSCULAS sem usar .upper():
    1. Percorro cada caractere de 'texto' com o for.
    2. Pego o código dele na tabela ASCII com ord():
       - 'a' a 'z' vai de 97 a 122
       - 'A' a 'Z' vai de 65 a 90
    3. Se o código está entre 97 e 122 (é minúscula),
       subtraio 32 para cair no código da mesma letra maiúscula.
       Ex: ord('b') = 98 -> 98 - 32 = 66 -> chr(66) = 'B'
    4. Converto de volta com chr() e imprimo sem pular linha.
"""
texto = input("Digite o texto: ")

# a variável 'i' vai assumir cada caractere de 'texto' a cada iteração do for
for i in texto:
    # obtenho o código do caratere na tabela ASCII
    code = ord(i)

    """ 
    caso o código esteja entre os códigos das letras minúsculas subtraio 32 
    para se tornar o código da mesma letra porém maiúscula """

    if 97 <= code <= 122:
        code -= 32

    # converto novamente o código em caractere
    print(chr(code), end="")