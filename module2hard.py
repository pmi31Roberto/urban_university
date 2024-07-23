n = int(input('Введите число от 3 до 20:'))
good = []
results = ''
for i in range(1, n):
    for j in range(1, n):
        if n % (i + j) == 0 and i != j and (str(j) + ' ' + str(i)) not in results:
            results += '  ' + str(i) + ' ' + str(j)
            # print(f'{i}{j}', end='')
    if i > (n / 2):
        break
results = results.replace(' ', '')
print(results)


#   1 2  1 4  1 14  2 3  2 13  3 12  4 11  5 10  6 9  7 8 //15 моё
#   1 2  1 4  1 14  2 3  2 13  3 12  4 11  5 10  6 9  7 8 //15 твоё
#   1 4  1 9  2 3  2 8  3 7  4 6 //10 моё
#   1 4  1 9  2 3  2 8  3 7  4 6 //10 твоё
#   1 3  1 4  1 9  1 19  2 3  2 8  2 18  3 7  3 17  4 6  4 16  5 15  6 14  7 13  8 12  9 11 //20 моё
#   1 3  1 4  1 9  1 19  2 3  2 8  2 18  3 7  3 17  4 6  4 16  5 15  6 14  7 13  8 12  9 11 //20 твоё

