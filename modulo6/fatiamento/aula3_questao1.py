numeros = []

print("Digite os números inteiros. (Digite 'parar' para encerrar)")

while True:
    entrada = input("Digite um número: ")
    
    if entrada.lower() == 'parar':
        if len(numeros) < 4:
            print("Erro: Você precisa digitar pelo menos 4 números para continuar.")
            continue
        break
    
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite apenas números inteiros ou 'parar'.")

print("\n------ Resultados ------")
print(f"Lista original: {numeros}")

print(f"Os 3 primeiros elementos: {numeros[:3]}")

print(f"Os 2 últimos elementos: {numeros[-2:]}")

print(f"A lista invertida: {numeros[::-1]}")

print(f"Elementos de índice par (0, 2, 4 ...): {numeros[::2]}")

print(f"Elementos de índice ímpar (1, 3, 5 ...): {numeros[1::2]}")