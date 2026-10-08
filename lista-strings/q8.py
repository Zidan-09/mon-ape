""" Remove todas as vogais do texto sem usar .replace():
    1. Percorro cada caractere de 'text' com o for.
    2. Converto para minúscula com .lower() para comparar sem
       diferenciar 'A' de 'a', e verifico se NÃO está na lista
       ["a", "e", "i", "o", "u"].
    3. Uso o condicional inline para montar 'final':
       final += i se não é vogal, senão soma "" (ou seja, pula).
       Ex: "monitoria" -> "mntr".
    4. No fim imprimo 'final' já sem vogais.
"""
text = input("Digite o texto: ")

final = ""

for i in text:
    final += i if i.lower() not in ["a", "e", "i", "o", "u"] else ""

print(final)