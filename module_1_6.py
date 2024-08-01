#Словарь
my_dick = {'Tagir': 1994, 'Adelina': 1999, 'Amirkhan': 2023}
print('Мой словарь: ', my_dick)
selected_key = input('Введите ключ из словаря значение которого необходимо вывести: ')
print('Выбранное значение', my_dick.get(selected_key))
print(my_dick.get('Sasha'), 'Такого имени нет в словаре')
my_dick['Kamil'] = 2000
my_dick.update({'Misha': 2001})
selected_key = input('Введите ключ из словаря значение которого необходимо вынуть из словаря: ')
print('Значеие ключа ', "'",selected_key,"' : ", my_dick.pop(selected_key))
print('Модифицированный словарь: ', my_dick)
#Множество
my_set = {1,2,5,92,1,2,5,9,2, 'str', 'int', 'str', True}
print('Множество: ',my_set)
my_set.add(3.3)
my_set.add(False)
my_set.discard(2)
print('Измененное множество: ',my_set)