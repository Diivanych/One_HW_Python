'''
import random
n = int(input('Введите количество элементов в массиве: '))
lst = []
for _ in range(n):
    lst.append(random.randint(-5, 5))
print(*lst)
lst.reverse()
print(*lst)
'''

'''

lst = [3, -5, -5, 1, -3, -3, -1, 1, 2, 4]
print(*lst)
lst.reverse()
print(*lst)

'''
'''

import random
n = int(input('Введите количество элементов в массиве: '))
lst = []
for _ in range(n):
    lst.append(random.randint(1, 5))
print(*lst)
minn = lst[0]
maxx = lst[0]
ind_maxx = []
# i = 1
for val in lst:
    if maxx < val:
        maxx = val
    if minn > val:
        minn = val
for i in range(n):
    if maxx == lst[i]:
        ind_maxx.append(i)

for i in range(len(ind_maxx)):
        lst[ind_maxx[i]] = minn        
        
print(f'максимальное число: {maxx}')
print(f'максимальный индексы: {ind_maxx}')
print(f'минимальное число: {minn}')
print(*lst)

'''

n = int(input("Введите число ")) 
lst = []
for i in range(int(n / 2)):
    i+=1     
    if (n % i) != 0:
        lst.append(i)

print(lst)