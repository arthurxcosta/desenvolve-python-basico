with open("frase.txt", "r", encoding="utf-8") as arquivo_entrada:
    texto = arquivo_entrada.read()

palavras_brutas = texto.split()
palavras_limpas = []

for palavra in palavras_brutas:
    palavra_filtrada = "".join([char for char in palavra if char.isalpha()])

    if palavra_filtrada:
        palavras_limpas.append(palavra_filtrada)

with open("palavras.txt", "w", encoding="utf-8") as arquivo_saida:
    for palavra in palavras_limpas:
        arquivo_saida.write(palavra + "\n")

with open("palavras.txt", "r", encoding="utf-8") as arquivo_leitura:
    print(arquivo_leitura.read().strip())