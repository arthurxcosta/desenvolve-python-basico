frase = input("Digite uma frase: ")

vogais = sorted([char for char in frase if char in 'aeiouAEIOUáãâÁÃÂÓÍíóôõêÊúÚàÀ'])

consoantes = [char for char in frase if char not in 'aeiouAEIOUáãâÁÃÂÓÍíóôõêÊúÚàÀ!?,.;:<>/-_' and char != ' ']


print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")