import csv
import os

# 1: Garantir que o Python encontra o ficheiro
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
nome_arquivo = os.path.join(diretorio_atual, "spotify-2023.csv")

# 2: Leitura do ficheiro com a codificação 'latin-1' pedida no enunciado
with open(nome_arquivo, "r", encoding="latin-1") as file:
    leitor = csv.reader(file)
    cabeçalho = next(leitor)  # Ignora o cabeçalho

    # Dicionário para armazenar a música mais tocada de cada ano no intervalo de 2012 a 2022
    # Formato: {ano: [track_name, artist_name, released_year, streams]}
    mais_tocadas_por_ano = {}

    for linha in leitor:
        # Garante que a linha possui colunas suficientes
        if len(linha) < 9:
            continue

        track_name = linha[0]
        artist_name = linha[1]

        # Tentar converter o ano e o número de streams para números inteiros
        try:
            released_year = int(linha[3])
            streams = int(linha[8])
        except ValueError:
            # Caso o valor de streams ou ano seja inválido/texto, salta a linha
            continue

        # Regra do exercício: filtrar apenas os anos de 2012 a 2022
        if 2012 <= released_year <= 2022:

            # Regra do exercício: ignorar músicas cujo nome contenha vírgulas ou aspas
            if "," in track_name or '"' in track_name:
                continue

            # Se o ano ainda não está no dicionário ou se encontramos uma música com mais streams nesse ano
            if (
                released_year not in mais_tocadas_por_ano
                or streams > mais_tocadas_por_ano[released_year][3]
            ):
                mais_tocadas_por_ano[released_year] = [
                    track_name,
                    artist_name,
                    released_year,
                    streams,
                ]

# 3: Ordenar a lista final por ano (de 2012 a 2022)
resultado_final = [
    mais_tocadas_por_ano[ano] for ano in sorted(mais_tocadas_por_ano.keys())
]

# 4: Imprimir a lista resultante
print("=== MÚSICAS MAIS TOCADAS POR ANO (2012 - 2022) ===")
print(resultado_final)