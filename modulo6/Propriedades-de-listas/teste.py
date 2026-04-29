notas = [90, 74, 82, 80, 68, 90]
soma = 0
for n in notas:
    soma += n
print("A soma das notas é: %d" % soma)



notas = [98, 74, 82, 80, 68, 90]
tamanho = len(notas)
print(tamanho)



notas = [90, 74, 82, 80, 68, 90]
soma = 0
tamanho = len(notas)
for i in range(tamanho):
    soma += notas[i]
print("A soma das notas é: %d" % soma)



notas = [90, 74, 82, 80, 68, 90]
print(98 in notas)
print(-1 in notas)
print(80 in notas)



nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(int(sum(nums)/len(nums)))



nums = [3,41, 12, 9, 3, 74, 15]
print(nums.index(74))
print(nums.index(3))



nums = [3,41, 12, 9, 3, 74, 15]
print(nums.count(3))



nums = [3,41, 12, 9, 3, 74, 15]
nums.sort()
print(nums)



nums = [3,41, 12, 9, 3, 74, 15]
print(sorted(nums))



a = [0,2, 3, 2]
x = a.remove(2)
print(a)
print(x, type(x))



a = [0, 2, 3, 2]
x= a.pop(2)
print(a)
print(x, type(x))