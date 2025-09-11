def inverteValor(numero):                                               # Cria a função que recebe um número inteiro
    invertido = 0                                                       # Variável para armazenar o número invertido
    while numero > 0:                                                   # Enquanto ainda houver dígitos no número...
        digito = numero % 10                                            # Pega o último dígito do número (ex: 123 % 10 = 3)
        invertido = invertido * 10 + digito                             # Move os dígitos do invertido para a esquerda e adiciona o novo
        numero = numero // 10                                           # Remove o último dígito (ex: 123 // 10 = 12)
    return invertido                                                    # Retorna o número invertido

def verificaInverso(original, invertido):                               # Cria função com dois números
    return(original % 2 == invertido % 2)                               # Retorna True ou False com base na igualdade de paridade  # Se os dois números são pares (resto 0) ou ímpares (resto 1), retorna True

valor = int(input('Digite um número inteiro: '))                        # Pede o número ao usuário

valor_invertido = inverteValor(valor)                                   # Usa a função para inverter o número
print(f'Valor invertido: {valor_invertido}')                            # Mostra o número invertido

igual_paridade = verificaInverso(valor, valor_invertido)                # Verifica se os dois têm mesma paridade
print(f'Mesma paridade (ambos pares ou ímpares)? {igual_paridade}')     # Mostra True ou False 