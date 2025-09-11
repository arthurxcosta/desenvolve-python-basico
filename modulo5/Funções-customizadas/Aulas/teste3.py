def func():
    global x # Se remover essa função (global) x passa a estar apenas dentro do escopo, assim somente o x da função tem o valor de 1, enquanto o x do código pricipal é 10.
    x = 1
    print('Na função:', x)

x = 10
func()
print('No código principal:', x)