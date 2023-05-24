
'''
phonebook = {
    '123': ['ЛИТВИНОВ', 'ДМИТРИЙ', 'ИВАНОВИЧ'],
    '456': ['СТАШЕНКО', 'РОМАН', 'КОНСТАНТИНОВИЧ'],
    '789': ['РЫКУНОВ', 'ИГОРЬ', 'ВЛАДИМИРОВИЧ'],
    '159': ['СТАШЕНКО', 'КОНСТАНТИН', 'РОМАНОВИЧ'],
}
'''
phonebook = open('file.txt', 'r')
#data.writelines(phonebook)
#data.close()

#for num in phonebook:
#    print(f'№ {num}. Владелец -', *phonebook[num])
print(phonebook)
phonebook.close()