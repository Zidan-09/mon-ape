""" Converte um número decimal para hexadecimal (maiúsculo) sem usar hex():
    1. Se value == 0, imprime "0" direto (caso especial).
    2. Senão, faço divisões sucessivas por 16:
       - pego o resto com value % 16 (temp vai de 0 a 15).
       - se temp < 10, vira str(temp) (0-9).
       - senão, vira letra com chr(ord("A") + temp - 10):
         Ex: 10 -> 'A', 11 -> 'B', ..., 15 -> 'F'.
       - somo em 'result' e atualizo value //= 16.
    3. Como os restos saem invertidos, monto 'final' percorrendo de trás
       para frente com range(len(result) - 1, -1, -1), igual ao q1.py.
    4. Imprimo 'final'.
       Ex: 255 -> restos "FF" invertido "FF" -> final "FF".
"""
value = int(input("Digite um valor: "))

result = ""

if value == 0:
    print("0")
    
else:
    result = ""

    while value > 0:
        temp = value % 16

        if temp < 10:
            result += str(temp)
        else:
            result += chr(ord("A") + temp - 10)

        value //= 16

    final = ""

    for i in range(len(result) - 1, -1, -1):
        final += result[i]

    print(final)