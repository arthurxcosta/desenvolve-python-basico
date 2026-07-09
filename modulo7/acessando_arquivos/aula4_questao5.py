livros = [
    ("A Guerra dos Tronos", "George R. R. Martin", 1996, 592),
    ("A Fúria dos Reis", "George R. R. Martin", 1998, 648),
    ("A Tormenta de Espadas", "George R. R. Martin", 2000, 832),
    ("O Festim dos Corvos", "George R. R. Martin", 2005, 608),
    ("A Dança dos Dragões", "George R. R. Martin", 2011, 824),
    ("Fogo e Sangue", "George R. R. Martin", 2018, 664),
    ("O Senhor dos Aneis", "J. R. R. Tolkien", 1954, 1795),
    ("O Cavaleiro dos 7 Reinos", "George R. R. Martin", 2014, 264),
    ("Dom Casmurro", "Machado de Assis", 1899, 208),
    ("O Alquimista", "Paulo Coelho", 1988, 208)
]

with open("meus_livros.csv", "w", encoding="utf-8") as ficheiro:

    ficheiro.write("Título,Autor,Ano de publicação,Número de páginas\n")

    for livro in livros:
        titulo = livro[0]
        autor = livro[1]
        ano = livro[2]
        paginas = livro[3]

        linha = f"{titulo},{autor},{ano},{paginas}\n"

        ficheiro.write(linha)

print("O ficheiro 'meus_livros.csv' foi criado com sucesso!")