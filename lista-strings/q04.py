""" Imprime apenas o pedaço texto[i:j] incluindo o índice j:
    1. Leio o texto e os índices I e J.
    2. Uso range(i, j + 1) porque o range para 1 antes do fim,
       então somo +1 para incluir o caractere da posição J.
       Ex: i=2, j=4 -> range(2, 5) gera [2, 3, 4]
    3. A cada iteração imprimo textoInserido[pedaco] sem pular linha.
    4. A versão comentada com while faz o mesmo:
       enquanto i <= j, imprime textoInserido[i] e faz i += 1.
"""
textoInserido = input("Digite o Texto: ")

i = int(input("Digite o valor de I: "))
j = int(input("Digite o valor de J: "))

for pedaco in range(i, j + 1):
    print(textoInserido[pedaco], end="")

""" while i <= j:
    print(textoInserido[i], end="")

    i += 1 """