""" Conta quantas vezes cada vogal aparece no texto (ignorando maiúscula/minúscula):
    1. Crio 5 contadores: a, e, i, o, u, todos começando em 0.
    2. Percorro cada caractere de 'text' com o for.
    3. Para cada 'char', comparo com as duas formas da vogal:
       Ex: se char == "a" or char == "A" -> a += 1
    4. Uso if/elif encadeado para somar só no contador correto.
    5. No fim imprimo os 5 totais com f-string.
"""
text = input("Digite o texto: ")

a = 0
e = 0
i = 0
o = 0
u = 0

for char in text:
    if char == "a" or char == "A":
        a += 1
    elif char == "e" or char == "E":
        e += 1
    elif char == "i" or char == "I":
        i += 1
    elif char == "o" or char == "O":
        o += 1
    elif char == "u" or char == "U":
        u += 1

print(f"Ocorrências de a: {a}, e: {e}, i: {i}, o: {o}, u: {u}")