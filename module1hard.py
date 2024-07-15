grades = [[5, 3, 3, 5, 4],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 3],
          [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print('начальное множество:', students)

_std_ = sorted(students)  # _std_ список по алфавиту
print('список по алфавиту:', _std_)

#словарь из 2 списков
result = dict(zip(_std_, map(lambda grades: sum(grades)/len(grades), grades)))
print(result)


