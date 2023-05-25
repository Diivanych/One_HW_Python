
import os
# Сам словарь
phonebook = {
    123: ['ЛИТВИНОВ', 'ДМИТРИЙ', 'ИВАНОВИЧ'],
    456: ['СТАШЕНКО', 'РОМАН', 'КОНСТАНТИНОВИЧ'],
    789: ['РЫКУНОВ', 'ИГОРЬ', 'ВЛАДИМИРОВИЧ'],
    159: ['СТАШЕНКО', 'КОНСТАНТИН', 'РОМАНОВИЧ'],
}

# Вывод словаря на экран
def view():
    for num in phonebook:
        print(f'№ {num}. Владелец -', *phonebook[num])

# Поиск по Номеру
def searchN():
    num = int(input('Введите искомый номер: '))
    if num in phonebook:
        print(f'№ {num}. Владелец -', *phonebook[num])
    else:
        print('Такого номера в справочнике нет.')

# Поиск по Фамилии
def searchF():
    surname = input('Введите искомую фамилию: ').upper()
    for num in phonebook:
        if surname in phonebook[num]:
            print(*phonebook[num], f'имеет номер {num}')
#        else:
#            print('Такого номера в справочнике нет.')

# Добавление новой записи в словарь
def app():
    ls = []
    num = int(input('Введите номер: '))
    ls.append(input('Введите фамилию: ').upper())
    ls.append(input('Введите имя: ').upper())
    ls.append(input('Введите отчество: ').upper())
    phonebook[num] = ls
    print(f'\n№ {num}. Владелец -', *phonebook[num])

# Редактирование записи
def edit():
    ls = []
    numdell = int(input('Введите номер записи для редактирования: '))
    print(f'\n№ {numdell}. Владелец -', *phonebook[numdell])
    num = int(input('Введите номер: '))
    ls.append(input('Введите фамилию: ').upper())
    ls.append(input('Введите имя: ').upper())
    ls.append(input('Введите отчество: ').upper())
    phonebook.pop(numdell)
    phonebook[num] = ls
    print(f'\n№ {num}. Владелец -', *phonebook[num])

def pr():
    print('\nВы используете учебный телефонный справочник.'
      '\nДля работы со справочником выберите следуещие действия:\n'
      '\n- Просмотреть  справочник   - введите "1"'
      '\n- Найти абонента по номеру  - введите "2"'
      '\n- Найти абонента по фамилии - введите "3"'
      '\n- Ввести  нового  абонента  - введите "4"'
      '\n- Изменить данные абонента  - введите "5"'
      '\n- Закончить работу со справочником - введите "0"\n'      
      )
os.system('cls')
pr()
sw = ''
while sw != 0:
    sw = input('\nСделайте Ваш выбор: ')
    os.system('cls')
    pr()
    if sw == '1':
        view()
    elif sw == '2':
        searchN()
    elif sw == '3':
        searchF()
    elif sw == '4':
        app()
    elif sw == '5':
        edit()
    elif sw == '0':
        os.system('cls')
        print('Всего хорошего!')
        break
    else:
        print('Неправильный выбор. Повторите ввод')
