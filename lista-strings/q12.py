""" Conta quantas vezes um trecho aparece dentro do texto sem usar .count():
    1. Leio o 'text' e o 'piece' (trecho procurado).
    2. Percorro os índices com range(len(text)).
    3. Em cada posição i, fatio text[i:i + len(piece)] (janela do mesmo
       tamanho do trecho) e comparo com 'piece'.
       Ex: text="banana", piece="ana" -> em i=1 e i=3 a fatia é "ana".
    4. Se igual, somo 1 no contador 'c'.
    5. No fim imprimo o total de ocorrências (conta sobreposições,
       pois avanço de 1 em 1).
"""
text = input("Digite o texto: ")
piece = input("Digite o trecho: ")

c = 0

for i in range(len(text)):
    if text[i:i + len(piece)] == piece:
        c += 1

print(f"Ocorrências de '{piece}': {c}")