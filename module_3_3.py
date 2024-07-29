def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_dict = {'a': 2, 'b': 3, 'c': 5}
values_list = [12, 'String', False]
values_list_2 = ['father', 23]

print_params(*values_list_2, 42)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

print_params(*values_list)
print_params(**values_dict)

print_params(a=25)
print_params(c=[1, 2, 3])
