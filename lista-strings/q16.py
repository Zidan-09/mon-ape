""" Converte um número decimal para qualquer base de 2 a 35 sem usar bibliotecas:
    1. Uso a string 'symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"'
       onde o índice é o valor do dígito.
       Ex: índice 10 -> 'A', índice 35 -> 'Z'.
    2. Se value == 0, imprime "0" direto (caso especial).
    3. Senão, faço divisões sucessivas pela base:
       - temp = value % base (resto da vez).
       - pego symbols[temp] e somo em 'result'.
       - atualizo value //= base.
       Ex: value=13, base=2 -> restos 1,0,1,1 -> result="1011" invertido.
    4. Como os restos saem invertidos, monto 'final' de trás para frente
       com range(len(result) - 1, -1, -1), igual ao q1.py.
    5. Imprimo 'final' na base pedida.
"""
value = int(input("Digite um valor: "))
base = int(input("Digite a base (2-35): "))

symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if value == 0:
    print("0")
else:
    result = ""

    while value > 0:
        temp = value % base
        result += symbols[temp]

        value //= base

    final = ""

    for i in range(len(result) - 1, -1, -1):
        final += result[i]

    print(final)