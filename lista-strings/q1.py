texto = input("Digite o texto: ")

""" O range segue a regra:
        1. De onde?
        2. Até onde?
        3. Em que passo?

    Ex: 
    range(0, 10, 1) vai gerar: [0, 1, 2, 3, 4, 5 , 6, 7, 8, 9]
    range(0, 10, 2) vai gerar: [0, 2, 4, 6, 8]
    range(10, 0, -1) vai gerar: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    nesse caso usei o 'len' para obter a quantidade de caracteres presentes no texto

    o valor obtido é subtraido por 1 para obter o índice correto

    então começo a montar o range:
        range(len(texto) - 1)

    ele deve ir até 0 
        - igualmente usamos 11 para ir até 10 (um a mais) aqui eu uso -1 para ir até 0 (um a menos)
    
    o range então fica:
        range(len(texto) - 1, -1)

    e para finalizar, quero que cada passo seja subtratindo o valor de 'len(texto) - 1' -1 vez:

    range(len(texto) - 1, -1, -1)
 """
for i in range(len(texto) - 1, -1, -1):
    print(texto[i], end="")