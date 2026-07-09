cpf_entrada = input("Digite o CPF (XXX.XXX.XXX-XX): ")

cpf_numeros = cpf_entrada.replace(".", "").replace("-", "")

if len(cpf_numeros) == 11 and cpf_numeros.isdigit():

    soma = 0
    multiplicador = 10

    for i in range(9):
        soma += int(cpf_numeros[i]) * multiplicador
        multiplicador -= 1
        
    resto = soma % 11
    if resto < 2:
        digito_1 = 0
    else:
        digito_1 = 11 - resto

    soma = 0
    multiplicador = 11

    for i in range(10):
        valor_atual = int(cpf_numeros[i]) if i < 9 else digito_1
        soma += valor_atual * multiplicador
        multiplicador -= 1
        
    resto = soma % 11
    if resto < 2:
        digito_2 = 0
    else:
        digito_2 = 11 - resto

    if str(digito_1) == cpf_numeros[9] and str(digito_2) == cpf_numeros[10]:
        print("Válido")
    else:
        print("Inválido")
        
else:
    print("Inválido")