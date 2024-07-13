my_dict = {'Robert': 2003, 'Tom': 1854}
print("Словарь:", my_dict)
# Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря
# my_dict без ошибки.
print('Существующее значение:', my_dict['Robert'])
print('Не существующее значение:', my_dict.get('Nat'))

my_dict.update({'Snake': 2000,
                'Woman': 2010})
print("Удаленное значение:", my_dict.get('Woman'))
del my_dict['Woman']
print("Измененный словарь:", my_dict)
print()


my_set = {1, 3, 3, 4, 4, 4, 3.3, True, '2 2 2'}
print('множество:', my_set)
print(my_set.update({16, 'Хочу практические работы сложнее'}))
print(my_set.remove(3))
print('Измененный множество:', my_set)
