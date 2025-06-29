# Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:
    # A: Para mulheres, ter mais de 60 anos. Para homens, 65.
    # B: Ou ter trabalhado pelo menos 30 anos
    # C: Ou ter 60 anos  e trabalhado pelo menos 25.

# Entrada de dados
genero  = input('Qual seu gênero (M ou F)? ')
idade   = int(input('Qual sua idade? '))
servico = int(input('Quanto tempo de serviço você tem (em anos)? '))

# Processamento
aposentar = ((genero == 'M' and (idade > 65 or servico >= 30)) or (idade >= 60 and servico >= 25)) or ((genero == 'F' and (idade > 60 or servico >= 30)) or (idade >= 60 and servico >= 25))

# Saída de dados
print('Você já pode se aposetar:', aposentar)