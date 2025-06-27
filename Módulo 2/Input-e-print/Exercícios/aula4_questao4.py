# Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente como indicado.

    # Entrada
        # 576

    # Saída
        # 5 nota(s) de R$100,00
        # 1 nota(s) de R$50,00
        # 1 nota(s) de R$20,00
        # 0 nota(s) de R$10,00
        # 1 nota(s) de R$5,00
        # 0 nota(s) de R$2,00
        # 1 nota(s) de R$1,00

# Leitura de dados (Entrada)
valor   = int(input("Digite o valor: "))

# Processamento de dados
    # Começar a calcular com a maior nota
nota100 = valor // 100 # 576 // 100 = 5
    # Atualizar o valor restante subtraindo o valor calculado anteriormente
valor   = valor % 100  # 576 - 5 * 100 = 76

nota50  = valor // 50 # 76 // 50 = 1
valor   = valor % 50  # 76 - 1 * 50 = 26

nota20  = valor // 20 # 26 // 20 = 1
valor   = valor % 20  # 26 - 1 * 20 = 6

nota10  = valor // 10 # 6 // 10 = 0
valor   = valor % 10  # 6 - 1 * 10 = 6

nota5   = valor // 5 # 6 // 5 = 1
valor   = valor % 5  # 6 - 1 * 10 = 1

nota2   = valor // 2 # 1 // 2 = 0
valor   = valor % 2  # 1 - 1 * 2 = 1

nota1   = valor // 1 # 1 // 1 = 1
valor   = valor % 1  # 1 - 1 * 2 = 0

# Impressão de dados (Saída)
print(f"{nota100} nota(s) de R$100,00")
print(f"{nota50} nota(s) de R$50,00")
print(f"{nota20} nota(s) de R$20,00")
print(f"{nota10} nota(s) de R$10,00")
print(f"{nota5} nota(s) de R$5,00")
print(f"{nota2} nota(s) de R$2,00")
print(f"{nota1} nota(s) de R$1,00")