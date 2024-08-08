def calculate_structure_sum(*args):
    summ = 0
    for i in args:
        if isinstance(i, tuple | list | set):
            summ += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            for key, value in i.items():
                summ += calculate_structure_sum(key)
                summ += calculate_structure_sum(value)
        elif isinstance(i, int | float):
            summ += i
        elif isinstance(i, str):
            summ += len(i)

    return summ


data_structure = [
 [1, 2, 3],
 {'a': 4, 'b': 5},
 (6, {'cube': 7, 'drum': 8}),
 "Hello",
 ((), [{(2, 'Urban', ('Urban2', 35))}])
 ]


result = calculate_structure_sum(data_structure)
print(result)


# i = {'a': 4, 'b': 5}
# for key, value in i.items():
#     print(key, value)
