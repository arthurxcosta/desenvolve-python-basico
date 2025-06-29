# Você é mestre de uma mesa de RPG e vai criar um sistema para validar uma ficha de personagem. Cada personagem tem uma classe específica com requisitos de atributos. Escreva um script que solicita a classe de personagem escolhida (guerreiro, mago ou arqueiro), os pontos de força e os pontos de magia atribuídos ao personagem. O programa deve imprimir True se os pontos de atributo são consistentes com a classe escolhida, seguindo as seguintes regras:
    # Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.
    # Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.
    # Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles pode ser superior a 15.
    # O programa deve imprimir False se os pontos de atributo não são consistentes com a classe escolhida.

# Entrada de dados
classe  = input("Escolha sua classe (guerreiro, mago ou arqueiro): ")
forca   = int(input("Digite seus pontos de força (1 a 20): "))
magia   = int(input("Digite seus pontos de magia (1 a 20): "))

# Processamento
validado = (classe == "guerreiro" and forca >= 15 and magia <= 10) or (classe == "mago" and forca <= 10 and magia >= 15) or (classe == "arqueiro" and forca > 5 and forca < 15 and magia > 5 and magia < 15)

# Saída de dados
print("Seus pontos de atributo são consistentes com a classe escolhida:", validado)