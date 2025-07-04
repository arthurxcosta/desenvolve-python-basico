### Você vai criar um sistema que registra os resultados dos jogos do Atlético MG ao longo de um campeonato. Seu sistema vai receber os resultados de todos os jogos do galo, e deve calcular a pontuação do time sabendo que vitórias valem 3 pontos, empates 1 ponto e derrotas 0 pontos.

## Entrada
# A primeira linha de entrada é um inteiro N com a quantidade de gols do galo e o segundo com a quantidade de gols do time oponente.

## Saída
# Apresente a soma de vitórias, empates e derrtotas do galo, junto com o cálculo da pontuação total.

n = int(input('Digite o número de jogos: '))
soma_vitorias   = 0
soma_empates    = 0
soma_derrotas   = 0

for jogo in range (n):
    gols_galo   = int(input('Quantos gols o galo fez? '))
    gols_adver  = int(input('Quantos gols o oponente fez? '))

    if gols_galo > gols_adver:
        soma_vitorias += 1
    elif gols_galo < gols_adver:
        soma_derrotas += 1
    else:
        soma_empates += 1

print('Total de vitórias: ', soma_vitorias)
print('Total de empates: ', soma_empates)
print('Total de derrotas: ', soma_derrotas)
print('Pontuação total: ', 3 * soma_vitorias + soma_empates)