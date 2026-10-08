""" Inverte os bits de um texto de 0s e 1s (complemento de 1) sem libs:
    1. Leio 'text' que deve conter só "0" e "1".
    2. Percorro cada caractere com o for.
    3. Se é "0", imprimo "1"; senão (é "1"), imprimo "0", com end=""
       para montar na mesma linha.
       Ex: "0101" -> "1010".
    4. A linha comentada faz o mesmo em 1 linha com ternário:
       print("1" if i == "0" else "0", end="").
"""
text = input("Digite um texto de 0s e 1s: ")

for i in text:
    if i == "0":
        print("1", end="")
    else:
        print("0", end="")

    # print("1" if i == "0" else "0", end="")