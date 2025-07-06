n1 = float(input('Digite o primeiro número decimal: '))
n2 = float(input('Digite o segundo número decimal: '))

diferenca = abs(n1 - n2)
diferenca_round = round(diferenca, 2)

print(f'A diferença absoluta entre os números é: {diferenca_round}')