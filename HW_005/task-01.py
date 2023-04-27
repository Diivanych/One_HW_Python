'''
Задача 26:  
Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
'''

a = int(input('Введите основание: '))
b = int(input('Введите показатель степени: '))

def exponent(base, exp):
    if exp == 1:
        return base
    else:
        return base * exponent(base, exp - 1)
    
print(exponent(a, b)) 
