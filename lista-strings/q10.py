""" Remove espaços duplicados, deixando só 1 espaço entre palavras, sem usar split/join:
    1. Percorro cada caractere de 'text' e vou montando 'final'.
    2. Se o caractere atual é " " E o último já adicionado (final[-1]) também é " ",
       é espaço repetido -> dou continue (pulo, não adiciono).
       Ex: "oi   mundo" -> os 2º e 3º espaços são pulados.
    3. Caso contrário, adiciono o caractere em 'final'.
    4. No fim imprimo 'final' com espaços simples.
       Atenção: se o texto começa com espaço, final[-1] no primeiro espaço
       dá erro de índice vazio - nesse caso inicialize final com o 1º char
       ou trate texto vazio antes do loop.
"""
text = input("Digite o texto: ")
final = ""

for i in text:
    if i == " " and final[-1] == " ":
        continue

    else:
        final += i

print(final)