'''
Задача 18: 
Требуется найти в массиве A самый близкий по величине элемент к заданному числу X. 
Если таких элементов несколько, вы вывести один любой. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). 
Последняя строка содержит число X

*Пример:*

5
    7 -2 3 5 1
    6
    -> 7
'''
import random
n = int(input('Введите количество элементов в массиве: '))
list = []
for _ in range(n):
    list.append(random.randint(-5,5))
print(*list)
x = int(input('Введите цифру для сравнения: '))
diff = abs(list[0] - x)
el = 0
for i in range(n):
    if diff > abs(list[i] - x):
        diff = abs(list[i] - x)
        el = i
print(list[el])
        
# print(f'Цифра {x}, в массиве А, встречается {count} раз')