'''
Задача №43. Решение в группах
Дан список чисел.  Посчитайте,  сколько  в  нем  пар
элементов, равных друг другу. Считается,  что  любые
два элемента, равные друг другу образуют одну  пару,
которую необходимо посчитать. Вводится список чисел. 
Все числа списка находятся на разных строках
'''
import random
numb = []
pairs = []
temp = ''

n = int(input('Введите количество элементов в массиве: '))
for _ in range(n):
    numb.append(random.randint(5, 9))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if numb[i] == numb[i + j]:
            temp = f'({numb[i]})'
#            if temp not in pairs:
            pairs.append(f'({numb[i]})')
#                break
print(*numb)
# print(*pairs) 
print(f'Количество пар в списке = {len(pairs)}') 








'''
for i in range(n - 2):
    for j in range(n - 3 - i):
        if numb[i] == numb[i + j + 2] and numb[i + 1] == numb[i + j + 3]:
            pairs.append(numb[i])
            pairs.append(numb[i + 1])
            pairs.append('||')
            break
print(*pairs) 
'''