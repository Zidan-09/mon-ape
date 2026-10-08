""" Remove as vogais do texto e imprime só consoantes (versão com lista):
    1. Crio a lista vogals = ["a", "e", "i", "o", "u"].
    2. Percorro cada caractere de 'text' com o for.
    3. Converto para minúscula com .lower() para ignorar 'A' vs 'a'
       e verifico se NÃO está em 'vogals'.
       Ex: 'E'.lower() = 'e' -> está na lista, então não imprime.
    4. Se não é vogal, imprimo com end="" para sair na mesma linha.
    5. A versão comentada de 1 linha faz o mesmo com condicional inline.
"""
text = input("Digite o texto: ")

vogals = ["a", "e", "i", "o", "u"]

# a variável 'i' vai assumir cada caractere de 'text' a cada iteração do for
for i in text:
    # Versão em 1 linha:
    # print(i if i.lower() not in ["a", "e", "i", "o", "u"] else "", end="")

    # Verifica se a letra atual NÃO está entre os elementos da lista 'vogals' e imprime se NÃO estiver.
    if i.lower() not in vogals:
        print(i, end="")