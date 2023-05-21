'''
1: 
Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
Примечание. Списки создайте вручную, например так:
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
'''

my_list_1 = [2, 2, 2, 5, 8, 8, 8, 2, 12, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
my_list_3 = []
# my_list_3 = list(set(my_list_1) - set(my_list_2))
for i in range(len(my_list_1)):
    if my_list_1[i] not in my_list_2:
        print(f'{my_list_1[i]}, ', end='')
        my_list_3.append(my_list_1[i])
print(my_list_3)