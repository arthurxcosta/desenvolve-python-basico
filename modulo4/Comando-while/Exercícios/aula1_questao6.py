n = int(input('Qual a quantidade de experimentos registrados: '))

cont = 0
sapo, rato, coelho, total = 0, 0, 0, 0

while cont < n:
    quantidade = int(input('Qual a quantidade de cobaias usadas nesse experimento? '))
    tipo    = input('Qual o tipo de cobaia usada (S, R ou C)? ')
    total += quantidade

    if tipo == 'S':
        sapo += quantidade
    elif tipo == 'R':
        rato += quantidade
    elif tipo == 'C':
        coelho += quantidade
    else:
        print('Tipo não cadastrado em nossa base de dados')

    cont += 1

print('Total de cobaias:', sapo + rato + coelho)
print('Total de sapos:', sapo)
print('Total de ratos:', rato)
print('Total de coelhos:', coelho)
print(f'Percentual de sapos: {sapo / total * 100:.2f} %')
print(f'Percentual de ratos: {rato / total * 100:.2f} %')
print(f'Percentual de coelho: {coelho / total * 100:.2f} %')