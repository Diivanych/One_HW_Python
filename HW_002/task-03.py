'''
Задача 14: 
Требуется вывести все целые степени двойки 
(т.е. числа вида 2k), не превосходящие числа N.
'''
n = int(input('Введите натуральное число: '))
k = 0
print('Ему соответствуют числа типа 2^k - ', end=' ')
while (2 ** k) <= n:
    print(2 ** k, end=' ')
    k +=1