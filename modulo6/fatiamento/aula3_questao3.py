import random

lista = [random.randint(-10, 10) for _ in range(20)]
lista_original = lista.copy()

max_inicio = 0
max_comprimento = 0

inicio_atual = 0
comprimento_atual = 0

for i, num in enumerate(lista):
    if num < 0:
        if comprimento_atual == 0:
            inicio_atual = i
        comprimento_atual += 1
    else:
        if comprimento_atual > max_comprimento:
            max_comprimento = comprimento_atual
            max_inicio = inicio_atual
        comprimento_atual = 0

if comprimento_atual > max_comprimento:
    max_comprimento = comprimento_atual
    max_inicio = inicio_atual

if max_comprimento > 0:
    del lista[max_inicio : max_inicio + max_comprimento]

print(f"Original: {lista_original}")
print(f"Editada: {lista}")

if max_comprimento > 0:
    print(f"\n O maior intervalo de negativos tinha {max_comprimento} elementos.")
else:
    print("\bNenhum número negativo foi encontrado na lista.")