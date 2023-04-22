'''
Задача 24: 
В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём 
кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное 
число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
'''
import random
n = int(input('Введите количество кустов на грядке: '))
numb = []
for _ in range(n):
    numb.append(random.randint(5, 9))
print(*numb)
k = int(input('С какого куста начнём? '))
m = int(input('Сколько модулей в собирающем блоке? '))
sum = 0
sums = []
for i in range(n):
    for j in range(m):
        sum += numb[(i + j + k - 1 - (m // 2)) % n]
    sums.append(sum)
    sum = 0
print(*sums)
print(max(sums))