'''
У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать): 
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

Ввод:
'''
'''
values = [1, 23, 42, 'asdfg']
def transformed(x for x in values):
    

transformed_values = list(map(trasformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')

'''

def progress(fst, diff, amt, res=[]):
    if amt < 1:
        print("amount exception")
        return None

    res.append(fst)

    if amt == 1:
        return res

    return progress(fst + diff, diff, amt - 1, res)


print(progress(fst=2, diff=2, amt=7))



''' Задача №49. 
Решение в группах
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи 
(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
'''
# Сам словарь
phonebook = {
    123: ['ЛИТВИНОВ', 'ДМИТРИЙ', 'ИВАНОВИЧ'],
    456: ['СТАШЕНКО', 'РОМАН', 'КОНСТАНТИНОВИЧ'],
    789: ['РЫКУНОВ', 'ИГОРЬ', 'ВЛАДИМИРОВИЧ'],
    159: ['СТАШЕНКО', 'КОНСТАНТИН', 'РОМАНОВИЧ'],
}
'''
# Вывод словаря на экран
for num in phonebook:
    print(f'№ {num}. Владелец -', *phonebook[num])

# Поиск по Фамилии
def searchF():
surname = input('Введите искомую фамилию: ').upper()
for num in phonebook:
    if surname in phonebook[num]:
        print(*phonebook[num], f'имеет номер {num}')

# Поиск по Номеру
def searchN():
    num = int(input('Введите искомый номер: '))
    if num in phonebook:
        print(f'№ {num}. Владелец -', *phonebook[num])
'''
# Добавление нового элемента в словарь
ls = []
num = int(input('Введите номер: '))
ls.append(input('Введите фамилию: ').upper())
ls.append(input('Введите имя: ').upper())
ls.append(input('Введите отчество: ').upper())
phonebook[num] = ls
for num in phonebook:
    print(f'№ {num}. Владелец -', *phonebook[num])
