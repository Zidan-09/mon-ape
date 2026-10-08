""" Converte um número decimal para algarismo romano:
    1. Crio a tabela 'values' em ordem decrescente com os pares
       (valor, símbolo), incluindo as formas subtrativas:
       1000-M, 900-CM, 500-D, 400-CD, 100-C, 90-XC,
       50-L, 40-XL, 10-X, 9-IX, 5-V, 4-IV, 1-I.
    2. Para cada (number, symbol) da tabela, enquanto value >= number:
       somo o símbolo em 'result' e subtraio value -= number.
       Ex: 1994 -> M (1000) + CM (900) + XC (90) + IV (4) = "MCMXCIV".
    3. Como a tabela já está do maior para o menor, o resultado
       sai na ordem correta sem precisar inverter.
    4. Imprimo 'result' com o numeral romano.
"""
value = int(input("Digite um valor: "))

values = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
]

result = ""

for number, symbol in values:
    while value >= number:
        result += symbol
        value -= number

print(result)