'''
Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
'''
import random

n = int(input('Введите количество элементов в первом массиве: '))
numb1 = []
for _ in range(n):
    numb1.append(random.randint(0, 9))

m = int(input('Введите количество элементов во втором массиве: '))
numb2 = []
for _ in range(m):
    numb2.append(random.randint(0, 9))

print(*numb1)
print(*numb2)

lst = []
for i in range(n):
    if numb1[i] not in numb2:
        lst.append(numb1[i])
        
print(*lst)

'''
lst = set(numb1) - set(numb2)
print(*lst)
lst = set(numb1).difference(set(numb2))
print(*lst)
'''