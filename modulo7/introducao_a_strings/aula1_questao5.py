frase = input("Digite uma frase: ")

quantidade_vogais = 0
indices = []

for i in range(len(frase)):
    letra = frase[i].lower()
    
    if letra in "aeiou":
        quantidade_vogais += 1
        indices.append(i)

print(f"{quantidade_vogais} vogais")
print(f"Índices {indices}")