'''
Задача 32: 
Определить индексы элементов массива (списка), значения которых 
принадлежат заданному диапазону (т.е. не меньше заданного минимума 
и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
'''
import random

n = int(input('Введите количество членов ряда: '))
numb = []
for _ in range(n):
    numb.append(random.randint(-9, 9))
print(*numb)

left_lim = int(input('Введите левый лимит: '))
right_lim = int(input('Введите правый лимит: '))

for i in range(n):
    if left_lim <= numb[i] <= right_lim:
        print(f'({i}:{numb[i]}), ', end='')
        