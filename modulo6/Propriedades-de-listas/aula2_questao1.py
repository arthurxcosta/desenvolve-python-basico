import random

# Gerando a lista
lista_original = [random.randint(-100, 100) for _ in range(20)]


# 1 - Imprimindo a lista ordenada, sem modificar a lista original
lista_ordenada = sorted(lista_original)
print(f"Lista ordenada: {lista_ordenada}")

# 2 - Imprimindo a lista original
print(f"Lista original: {lista_original}")

# 3 - Imprimindo o índice do maior valor da lista
maior_valor = max(lista_original)
indice_maior = lista_original.index(maior_valor)
print(f"Índice do maior valor ({maior_valor}): {indice_maior}")

# 4 - Imprimindo o índice do menor valor da lista
menor_valor = min(lista_original)
indice_menor = lista_original.index(menor_valor)
print(f"Índice do menor valor ({menor_valor}): {indice_menor}")