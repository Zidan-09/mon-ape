""" Remove os espaços do início e do fim do texto sem usar .strip():
    1. Começo com start = 0 (primeiro índice) e end = len(text) - 1 (último índice).
    2. Enquanto text[start] == " ", avanço start += 1 para pular espaços da esquerda.
    3. Enquanto text[end] == " ", recuo end -= 1 para pular espaços da direita.
       Ex: "   oi   " -> start para no 'o' (índice 3) e end para no 'i'.
    4. Fatio text[start:end + 1] (+1 porque o fatiamento exclui o fim)
       e imprimo entre aspas simples para visualizar.
    5. A versão comentada faz o mesmo com for + range(start, end + 1)
       concatenando caractere por caractere.
"""
text = input("Digite o texto: ")

start = 0
end = len(text) - 1

while text[start] == " ":
    start += 1

while text[end] == " ":
    end -= 1

final = text[start:end + 1]

print(f"'{final}'")

# Outra opção sem fatiamento:

""" final = ""

for i in range(start, end + 1):
    final += text[i]

print(f"'{final}'") """