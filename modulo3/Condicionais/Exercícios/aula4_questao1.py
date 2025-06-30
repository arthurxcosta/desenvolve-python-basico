# Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar. Lembre-se do operador do python % que retorna o resto de uma divisão. 

# Entrada de dados
num_1   = int(input('Digite o primeiro número: '))
num_2   = int(input('Digite o segundo número: '))

# Processamento
soma    = num_1 + num_2
soma    = soma // 2
soma    = soma % 2

# Saída de dados
if soma == 0:
    print('O número é par.')
else:
    print('O número é impar.')