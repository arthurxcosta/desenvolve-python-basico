import random

def encrypt(lista_nomes):
    chave = random.randint(1, 10)
    
    nomes_cript = []

    for nome in lista_nomes:
        nome_criptografado = ""

        for c in nome:
            novo_valor = ord(c) + chave

            if novo_valor > 126:
                novo_valor = 33 + (novo_valor - 127)

            nome_criptografado += chr(novo_valor)
            
        nomes_cript.append(nome_criptografado)

    return nomes_cript, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)

print(f"nomes = {nomes}")
print(f"chave_aleatoria = {chave_aleatoria}")
print(f"nomes_cript = {nomes_cript}")