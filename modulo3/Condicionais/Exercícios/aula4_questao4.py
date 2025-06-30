# Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
    # Distância até 100 km: R$1 por kg.
    # Distância entre 101 e 300 km: R$1.50 por kg.
    # Distância acima de 300 km: R$2 por kg.
    # Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

distancia   = float(input('Qual a distância da entrega (em quilômetros)? '))
peso        = float(input('Qual o peso do pacote (em quilogramas)? '))

if distancia <= 100:
    preco = 1.0
elif distancia <= 300:
    preco = 1.5
else:
    preco = 2.0

frete = peso * preco

if peso > 10:
    frete += 10

print(f"Valor do frete: R${frete:.2f}")