# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# ------------------------------------------------------------------------------

print()
height = int(input('Введите высоту шоколадки: '))
width = int(input('Введите ширину шоколадки: '))
greed = int(input('Сколько долек  Вам нужно? '))
while greed % height != 0 and greed % width != 0 or greed >= height * width:
    print('\nПридумай чего по-проще.')
    greed = int(input('Попробуй ещё раз.   '))
else:
    print('\nДа запросто! Берите. \n ')