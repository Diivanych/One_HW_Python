'''
Задача 12: 
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных 
числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя 
делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
'''
s = int(input('Катя, запиши. Сумма двух чисел S = '))
p = int(input('А произведение этих чисел P = '))
for x in range(s):
    for y in range(p):
        if x + y == s and x * y == p:
            print(f'Это пара чсел X = {x} и Y = {y}')
            break
    else:
        continue
    break
else:
    print('Для такой пары чисел решения нет')