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
