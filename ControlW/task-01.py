
import json
import time
import datetime
import os

# Сам словарь
note = {
    123: ['О ТЕСТИРОВАНИИ ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ', 'ПРЕЖДЕ ЧЕМ НОВАЯ ВЕРСИЯ КОМПЬЮТЕРНОЙ ПРОГРАММЫ, САЙТА ИЛИ МОБИЛЬНОГО ПРИЛОЖЕНИЯ ПОПАДАЕТ К ПОЛЬЗОВАТЕЛЮ, ОНА ДОЛЖНА ПРОЙТИ ЧЕРЕЗ РУКИ ИНЖЕНЕРОВ-ТЕСТИРОВЩИКОВ. ОНИ ИЩУТ МЕСТА В КОДЕ, ГДЕ ПРОГРАММА РАБОТАЕТ НЕ ТАК, КАК ЗАДУМАНО. ЧТОБЫ НАЙТИ КАК МОЖНО БОЛЬШЕ ОШИБОК, ТЕСТИРОВЩИКИ МОДЕЛИРУЮТ РАЗНЫЕ СИТУАЦИИ, КОТОРЫЕ МОГУТ ВОЗНИКНУТЬ ПРИ ИСПОЛЬЗОВАНИИ ПРИЛОЖЕНИЯ.', 1489832481.870589],
    456: ['О РАЗРАБОТКЕ ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ', 'РАЗРАБОТКА ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ-ЭТО ПРОЦЕСС РАЗРАБОТКИ, УТОЧНЕНИЯ, ПРОЕКТИРОВАНИЯ, ПРОГРАММИРОВАНИЯ, ДОКУМЕНТИРОВАНИЯ, ТЕСТИРОВАНИЯ И ИСПРАВЛЕНИЯ ОШИБОК, СВЯЗАННЫХ С СОЗДАНИЕМ И ПОДДЕРЖКОЙ ПРИЛОЖЕНИЙ, ФРЕЙМВОРКОВ ИЛИ ДРУГИХ ПРОГРАММНЫХ КОМПОНЕНТОВ.', 1689832221.270589],
    789: ['О СТЕКАХ В PYTHON', 'СТЕК В PYTHON – ЭТО ЛИНЕЙНАЯ СТРУКТУРА ДАННЫХ, В КОТОРОЙ ДАННЫЕ РАСПОЛОЖЕНЫ ОБЪЕКТАМИ ДРУГ НАД ДРУГОМ. ОН ХРАНИТ ДАННЫЕ В РЕЖИМЕ LIFO (LAST IN FIRST OUT). ДАННЫЕ ХРАНЯТСЯ В ТОМ ЖЕ ПОРЯДКЕ, В КАКОМ НА КУХНЕ ТАРЕЛКИ РАСПОЛАГАЮТСЯ ОДНА НАД ДРУГОЙ. МЫ ВСЕГДА ВЫБИРАЕМ ПОСЛЕДНЮЮ ТАРЕЛКУ ИЗ СТОПКИ ТАРЕЛОК. В СТЕКЕ НОВЫЙ ЭЛЕМЕНТ ВСТАВЛЯЕТСЯ С ОДНОГО КОНЦА, И ЭЛЕМЕНТ МОЖЕТ БЫТЬ УДАЛЕН ТОЛЬКО С ЭТОГО КОНЦА.',  1289832861.670589],
    159: ['О ТЕКСТОВЫХ ФАЙЛАХ', 'ЭТО ФАЙЛЫ С ЧЕЛОВЕКОЧИТАЕМЫМ СОДЕРЖИМЫМ. В НИХ ХРАНЯТСЯ ПОСЛЕДОВАТЕЛЬНОСТИ СИМВОЛОВ, КОТОРЫЕ ПОНИМАЕТ ЧЕЛОВЕК. БЛОКНОТ И ДРУГИЕ СТАНДАРТНЫЕ РЕДАКТОРЫ УМЕЮТ ЧИТАТЬ И РЕДАКТИРОВАТЬ ЭТОТ ТИП ФАЙЛОВ. ТЕКСТ МОЖЕТ ХРАНИТЬСЯ В ДВУХ ФОРМАТАХ: (.TXT) — ПРОСТОЙ ТЕКСТ И (.RTF) — «ФОРМАТ ОБОГАЩЕННОГО ТЕКСТА».', 1589832641.470589],
}

# Вывод словаря на экран
def view():
    print('\n================================================================================')
    for num in note:
        print(f'%11s' % num,
            '\n\n%-40s' %  note[num][0], '\n%s' %  note[num][1],
            '\n\n%30s' %  datetime.datetime.fromtimestamp(float(note[num][-1])).strftime("%B %d, %Y %I:%M:%S"),
            '\n================================================================================')

# Поиск по номеру заметки
def searchN():
    num = int(input('Введите искомый номер заметки: '))
    if num in note:
        print('\n================================================================================')
        print(f'%11s' % num,
            '\n\n%-40s' %  note[num][0], '\n%s' %  note[num][1],
            '\n\n%30s' %  datetime.datetime.fromtimestamp(float(note[num][-1])).strftime("%B %d, %Y %I:%M:%S"),
            '\n================================================================================')

# Поиск по заголовку заметки
def searchF():
    k = 0
    head = input('Введите фрагмент из заголовка: ').upper()
    print('\n================================================================================')
    for num in note:
        if head in note[num][0]:            
            print(f'%11s' % num,
                '\n\n%-40s' %  note[num][0], '\n%s' %  note[num][1],
                '\n\n%30s' %  datetime.datetime.fromtimestamp(float(note[num][-1])).strftime("%B %d, %Y %I:%M:%S"),
                '\n================================================================================')
            k = 1
    if k == 0:
        print('Нет такого слова в заголовке')
            
# Поиск по содержимому заметки
def searchName():
    k = 0
    body = input('Введите фрагмент из текста заметк: ').upper()
    print('\n================================================================================')
    for num in note:
        if body in note[num][1]:
            print(f'%11s' % num,
                '\n\n%-40s' %  note[num][0], '\n%s' %  note[num][1],
                '\n\n%30s' %  datetime.datetime.fromtimestamp(float(note[num][-1])).strftime("%B %d, %Y %I:%M:%S"),
                '\n================================================================================')
            k = 1
    if k == 0:
        print('Нет такого слова в тексте заметки')

# Сортировка по времени
def sortTime():
    tLs = []
    tMin = 0
    mov = 0
    for num in note:
        tMin = 0
        for num in note:
            if tMin < (note[num][2]) and num not in tLs:
                tMin = (note[num][2])
                mov = num
        tLs.append(mov)
    print('\n================================================================================')
    for i in range(len(tLs)):
        print(f'%11s' % tLs[i],'%30s' %  datetime.datetime.fromtimestamp(float(note[tLs[i]][-1])).strftime("%B %d, %Y %I:%M:%S"), '   %-50s' %  note[tLs[i]][0])

# Поиск за перод времени
def deltaTime():
    print('\nНа данный момент в базе хранится, ', len(note),' заметок.\n')
    sortTime()

    lowerYear = 0
    lowerMonth = 0
    lowerDey = 0

    upperYear = 3000
    upperMonth = 0
    upperDey = 0

    print('\nВедите начальную дату поиска.')
    lowerYear = int(input('\nВведите год "ГГГГ": '))
    lowerMonth = int(input('Введите месяц "ММ": '))
    lowerDey = int(input('Введите день  "ДД": '))
    lowerDate = datetime.datetime(lowerYear, lowerMonth, lowerDey).timestamp()
    print('\n',datetime.datetime.fromtimestamp(float(lowerDate)).strftime("%B %d, %Y"))

    print('\nВедите конечную дату поиска.')
    upperYear = int(input('\nВведите год "ГГГГ": '))
    upperMonth = int(input('Введите месяц "ММ": '))
    upperDey = int(input('Введите день  "ДД": '))
    upperDate = datetime.datetime(upperYear, upperMonth, upperDey).timestamp()
    print('\n',datetime.datetime.fromtimestamp(float(upperDate)).strftime("%B %d, %Y"))
    
    print('\n================================================================================')
    for num in note:
        if note[num][2] > lowerDate and note[num][2] < upperDate:
            print(f'%11s' % num,
            '\n\n%-40s' %  note[num][0], '\n%s' %  note[num][1],
            '\n\n%30s' %  datetime.datetime.fromtimestamp(float(note[num][-1])).strftime("%B %d, %Y %I:%M:%S"),
            '\n================================================================================')

# Добавление новой записи в словарь
def app():
    ls = []
    num = int(input('Введите номер заметки: '))
    ls.append(input('Введите тему заметки: ').upper())
    ls.append(input('Введите содержание заметки: ').upper())
    ls.append(time.time())
    note[num] = ls
    print('\n================================================================================')
    print(f'%11s' % num,
        '\n\n%-40s' %  note[num][0], '\n%s' %  note[num][1],
        '\n\n%30s' %  datetime.datetime.fromtimestamp(float(note[num][-1])).strftime("%B %d, %Y %I:%M:%S"),
        '\n================================================================================')

# Редактирование записи
def edit():
    ls = []
    numdell = int(input('Введите номер заметки для редактирования: '))
    print(f'\n№ {numdell}', *note[numdell])
    num = int(input('Введите номер заметки: '))
    ls.append(input('Введите тему заметки: ').upper())
    ls.append(input('Введите содержание заметки: ').upper())
    ls.append(time.time())
    note.pop(numdell)
    note[num] = ls
    print('\n================================================================================')
    print(f'%11s' % num,
        '\n\n%-40s' %  note[num][0], '\n%s' %  note[num][1],
        '\n\n%30s' %  datetime.datetime.fromtimestamp(float(note[num][-1])).strftime("%B %d, %Y %I:%M:%S"),
        '\n================================================================================')
    
# Удаление записи
def numDell():
    print('\nНа данный момент в базе хранится, ', len(note),' заметок.\n')
    sortTime()
    num = int(input('Введите номер заметки для удаления: '))
    print('\nУдаляется заметка')
    print('\n================================================================================')
    print(f'%11s' % num,
        '\n\n%-40s' %  note[num][0], '\n%s' %  note[num][1],
        '\n\n%30s' %  datetime.datetime.fromtimestamp(float(note[num][-1])).strftime("%B %d, %Y %I:%M:%S"),
        '\n================================================================================')
    note.pop(num)
    print('\nСостояние базы после удаления')
    sortTime()

# Запись в файл
def writeFile():
    with open('./notes.jon', 'w') as f:
        json.dump(note, f)
    print('\nДанные сохранены')

# Чтение из файла
def readFile():    
    global note
    with open('./notes.jon', 'r') as f:
        note = json.load(f)
    print('\nДанные приняты')
# Главное меню
def pr():
    print('\nВы используете учебный редактор заметок.'
      '\nДля работы со редактором заметок выберите следуещие действия:\n'
      '\n- Просмотреть все заметки       - введите "1"'
      '\n- Найти заметку по номеру       - введите "2"'
      '\n- Найти заметку по теме         - введите "3"'
      '\n- Найти заметку по содержанию   - введите "4"'
      '\n- Ввести новую заметку          - введите "5"'
      '\n- Редактировать старую заметку  - введите "6"'
      '\n- Сортировка заметок по дате    - введите "7"'
      '\n- Запись заметок в файл         - введите "8"'
      '\n- Чтение заметок из файла       - введите "9"'
      '\n- Поиск за перод времени        - введите"10"'
      '\n- Удаление заметки              - введите"11"'      
      '\n- Закончить работу с редактором - введите "0"\n'      
      )
os.system('cls')
pr()
sw = -1
while sw != 0:
    sw = int(input('\nСделайте Ваш выбор: '))
    os.system('cls')
    pr()
    if sw == 1:
        view()
    elif sw == 2:
        searchN()
    elif sw == 3:
        searchF()
    elif sw == 5:
        app()
    elif sw == 6:
        edit()
    elif sw == 4:
        searchName()
    elif sw == 7:
        sortTime()
    elif sw == 8:
        writeFile()
    elif sw == 9:
        readFile()
        print(note)
        print(type(note))
    elif sw == 10:
        deltaTime()
    elif sw == 11:
        numDell()
    elif sw == 0:
        os.system('cls')
        print('Всего хорошего!')
        break
    else:
        print('Неправильный выбор. Повторите ввод')
