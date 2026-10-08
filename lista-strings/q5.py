""" Converte o texto para Título (primeira letra de cada palavra maiúscula) sem usar .title():
    1. Percorro os índices com range(len(textoInserido)).
    2. Se é o índice 0 e não é espaço, é início do texto -> vira maiúscula.
    3. Senão, se o caractere atual não é espaço E o anterior é espaço,
       é início de palavra -> vira maiúscula com .upper().
       Ex: "oi mundo" -> o 'o' do índice 0 e o 'm' após o espaço viram 'O' e 'M'.
    4. Nos demais casos só copio o caractere original para 'textoFinal'.
    5. No fim imprimo o textoFinal já montado.
"""
textoInserido = input("Digite o Texto: ")
textoFinal = ""

# range: Gera lista de números, len: Descobre o tamanho do texto
for i in range(len(textoInserido)):
    # Checa se é a primeira letra do texto inteiro e se não é um espaço " "
    if i == 0 and textoInserido[i] != " ":
        textoFinal += textoInserido[i].upper()

    # Checa se o caractere atual NÃO é um espaço " " E se antes dele É um espaço " "
    elif textoInserido[i] != " " and textoInserido[i - 1] == " ":
        textoFinal += textoInserido[i].upper()

    # Se não é um caractere para ser maiúculo apenas repete
    else:
        textoFinal += textoInserido[i]

print(textoFinal)