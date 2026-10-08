""" Formata um número float no padrão brasileiro (ponto de milhar e vírgula decimal):
    1. Leio o valor como float e converto para string.
       Ex: 1234567.89 -> "1234567.89"
    2. Separo com split(".") em integerPart = "1234567" e decimalPart = "89".
    3. Percorro a parte inteira de trás para frente com:
       range(len(integerPart) - 1, -1, -1), igual ao q1.py,
       montando 'temp' como integerPart[i] + temp (insiro na frente).
    4. Conto cada dígito em 'c'; a cada 3 dígitos insiro "." na frente
       e zero o contador.
       Ex: "1234567" -> "1.234.567"
    5. No fim junto temp + "," + decimalPart e imprimo.
       Ex: "1.234.567,89"
"""
number = float(input("Digite o valor: "))

text = str(number)

integerPart, decimalPart = text.split(".")

temp = ""
c = 0

for i in range(len(integerPart) - 1, -1, -1):
    temp = integerPart[i] + temp

    c += 1

    if c == 3:
        temp = "." + temp
        c = 0

final = temp + "," + decimalPart

print(final)