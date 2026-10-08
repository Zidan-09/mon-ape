""" Conta quantas vezes o bit '1' aparece no texto binário:
    1. Leio 'text' que deve conter só "0" e "1".
    2. Crio o contador c = 0.
    3. Percorro cada caractere com o for; se i == "1", faço c += 1.
       Ex: "10111" -> conta 4.
    4. No fim imprimo o total com f-string.
"""
text = input("Digite um texto de 0s e 1s: ")

c = 0

for i in text:
    if i == "1":
        c += 1

print(f"Ocorrências de '1's: {c}")