### Observação -> Fiz de tudo para entender esse fluxograma, mas não consegui, desde o momento que li acreditei ter algo errado, então joguei no chat gpt para tentar entender, e ele também me apontou que a lógica indicava que o 'n < cont' na verdade teria de ser 'cont < n' para fazer sentido com o restante do comportamento do fluxograma, por isso a resposta está com 'cont < n'.


n = int(input('Digite o valor de n: '))
cont = 0

while cont < n:
    cont = cont + 1
    print(cont)

print('Fim')