import random

# Preenchendo as listas
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Criando a lista de intersecção
interseccao = sorted(list(set(lista1) & set(lista2)))

# Impressões
print(f"Lista 1 - {lista1}")
print(f"Lista 2 - {lista2}")
print(f"Intersecção - {interseccao}")

print("\nContagem")
for item in interseccao:
    qtd_lista1 = lista1.count(item)
    qtd_lista2 = lista2.count(item)
    print(f"{item}: (lista1={qtd_lista1}, lista2={qtd_lista2})")