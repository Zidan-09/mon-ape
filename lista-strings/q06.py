""" Troca todas as ocorrências de um caractere por outro sem usar .replace():
    1. Leio o texto, o 'target' (o que deve ser trocado)
       e o 'data' (o que vai substituir).
    2. Percorro cada caractere de 'text' com o for.
    3. Para cada 'i', uso o condicional inline:
       imprimo 'i' se i != target, senão imprimo 'data'.
       Ex: text="banana", target="a", data="o" -> imprime "bonono".
    4. Uso end="" para montar a saída na mesma linha.
"""
text = input("Digite o texto: ")

target = input("Digite o que deve ser trocado: ")
data = input("Digite o que vai substituir: ")

for i in text:
    print(i if i != target else data, end="")