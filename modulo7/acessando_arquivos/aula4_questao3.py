import os
import re

# Procurando o caminho da pasta onde este script .py está guardado
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
nome_arquivo = os.path.join(diretorio_atual, "estomago.txt")

with open(nome_arquivo, "r", encoding="utf-8") as file:
    linhas = file.readlines()

# 1: O texto das primeiras 25 linhas
print("=== PRIMEIRAS 25 LINHAS ===")
for i, linha in enumerate(linhas[:25], 1):
    linha_limpa = linha.rstrip('\n')
    print(f"{i}: {linha_limpa}")

# 2: Número de linhas do arquivo
num_linhas = len(linhas)
print(f"\nNúmero total de linhas: {num_linhas}")

# 3: Linha com maior número de caracteres
linha_mais_longa = max(linhas, key=len)
print(f"\nLinha com maior número de caracteres ({len(linha_mais_longa)} caracteres):")
print(f'"{linha_mais_longa.strip()}"')

# 4: Menções aos personagens "Nonato" e "Íria"
texto_completo = "".join(linhas)

padrao_nonato = r"\bnonato\b"
padrao_iria = r"\b[íi]ria\b"

mencoes_nonato = len(re.findall(padrao_nonato, texto_completo, re.IGNORECASE))
mencoes_iria = len(re.findall(padrao_iria, texto_completo, re.IGNORECASE))

print(f"\n=== CONTAGEM DE MENÇÕES ===")
print(f'Menções ao personagem "Nonato": {mencoes_nonato}')
print(f'Menções ao personagem "Íria": {mencoes_iria}')