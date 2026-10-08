""" Converte um número decimal para binário sem usar bin():
    1. Se value == 0, imprime 0 direto (caso especial).
    2. Senão, faço divisões sucessivas por 2:
       - pego o resto com value % 2 (vai ser 0 ou 1) e somo em 'result'.
       - atualizo com divisão inteira value = value // 2.
       Ex: 13 -> restos 1, 0, 1, depois value vira 1 -> encerra.
    3. Como os restos saem do menos significativo para o mais significativo,
       'result' fica invertido, então monto 'final' percorrendo de trás
       para frente com range(len(result) - 1, -1, -1), igual ao q1.py.
    4. Imprimo 'final', que é o binário na ordem correta.
       Ex: 13 -> "1011" invertido "1101" -> final "1011".
"""
value = int(input("Digite um valor: "))

result = ""

if value == 0:
    print(0)
else:
    while value > 0:
        result += str(value % 2)

        value = value // 2

        if value == 1:
            result += str(value)
            break

    final = ""

    for i in range(len(result) -1, -1, -1):
        final += result[i]

    print(final)