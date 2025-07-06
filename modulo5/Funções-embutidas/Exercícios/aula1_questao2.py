### Fiz um print com os valores gerados para conferir o resultado

import random
import math

n = int(input('Quantos números deseja gerar? '))

valores = []

for _ in range(n):
    valor = random.randint(0, 100)
    valores.append(valor)

soma = sum(valores)

raiz = math.sqrt(soma)

print(f'A raiz quadrada da soma dos valores é: {raiz:.2f}')
print(f'Valores gerados: {valores}')