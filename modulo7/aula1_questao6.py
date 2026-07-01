frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

objetivo_ordenado = sorted(palavra_objetivo.lower())

anagramas = []

for palavra in frase.split():
    if sorted(palavra.lower()) == objetivo_ordenado:
        anagramas.append(palavra)

saida_formatada = str(anagramas).replace("'", '"')

print(f"Anagramas: {saida_formatada}")