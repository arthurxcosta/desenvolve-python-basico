lista_pares = [x for x in range(20, 51) if x % 2 == 0]

lista_base = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_quadrados = [x ** 2 for x in lista_base]

lista_divisiveis_7 = [x for x in range(1, 101) if x % 7 == 0]

lista_paridade = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30, 3)]

# ----- 1
print("1. Números pares de 20 a 50:")
print(lista_pares)
print("-" * 40)

# ----- 2
print("2. Números quadrados da lista:")
print(lista_quadrados)
print("-" * 40)

# ----- 3
print("3. Números divisíveis por 7 de 1a 100:")
print(lista_divisiveis_7)
print("-" * 40)

# ----- 4
print("4. Paridade em range(0, 30, 3):")
print(lista_paridade)