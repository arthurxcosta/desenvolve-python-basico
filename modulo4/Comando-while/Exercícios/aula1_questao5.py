n = int(input('Digite a quantidade de respondentes: '))
soma = 0
cont = 0

while cont < n:
    idade = int(input('Digite a idade do respondente: '))
    soma += idade
    cont += 1

media = soma / n
print(f'A média das idades é {media} anos')