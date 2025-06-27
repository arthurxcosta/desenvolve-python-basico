# 1 - Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado como mostra o exemplo a seguir:

# O terreno possui 250m2 e custa R$512,490.50

# comprimento = 10
# largura = 25
# preco_m2 = 2049.97

# Leitura de dados (Entrada)
comprimento = int(input('Digite o comprimento do terreno? '))
largura     = int(input('Digite a largura do terreno? '))
preco_m2    = float(input('Digite o valor do m2? '))

# Processamento de dados
area_m2     = comprimento*largura
area_m2     = int(area_m2) # Conversão dos dados para inteiro
preco_total = preco_m2*area_m2
preco_total = float(preco_total) # Conversão dos dados para flutuante/decimal

# Impressão de dados (Saída)
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")