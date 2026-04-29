import random

# Gerando o valor aleatório de 5 a 20
num_elementos = random.randint(5, 20)

elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Calculando a soma e a média
soma_valores = sum(elementos)
media_valores = soma_valores / len(elementos)

# Impressões
print(f"Lista elementos: {elementos}")
print(f"Quantidade de itens gerados: {num_elementos}")
print(f"Soma dos valores da lista: {soma_valores}")
print(f"Média dos valores da lista: {media_valores: .2f}")