'''
2: 
Дана дата в формате dd.mm.yyyy, например: 02.11.2013. 
Ваша задача — вывести дату в текстовом виде, например: 
второе ноября 2013 года. 
Склонением пренебречь (2000 года, 2010 года)
'''

# dat = input('Введите дату в формате dd.mm.yyyy: ')

data = [1, 2, 3, 5, 8, 15, 23, 38]
out = []
for i in data :
    if i % 2 == 0:
        out.append((i, i ** 2))
print(out)

