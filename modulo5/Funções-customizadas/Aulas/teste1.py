def fatorial(valor):

    #corpo da função
    fat = 1
    for i in range(1, valor+1):
        fat *= i
    return fat

for n in range(1,6):
    meu_fatorial = fatorial(n)
    print(f'{n}! é {meu_fatorial}')