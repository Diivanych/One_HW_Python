import random
n = int(input('Введите количество элементов в массиве: '))
lst = []
for _ in range(n):
    lst.append(random.randint(-9, 9))
print(*lst)
a = max(lst)
print(max(lst))
print(min(lst))
lst.sort()
print(lst)
lst.reverse()
print(lst)
lst.insert(0, 17)
lst.insert(0, 27)
lst.insert(0, 39)
print(lst)
