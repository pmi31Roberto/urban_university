# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# not_primes = []
# for i in range(len(numbers)):
#     for j in range(2, numbers[i]):
#         if numbers[i] % j == 0:
#             not_primes.append(numbers[i])  # не простое
#             break
#
# primes = []
# for i in range(len(numbers)):
#     for j in range(2, numbers[i]):
#         if numbers[i] % j == 0:
#             break
#         else:
#             primes.append(numbers[i])
#             break
#
# print(not_primes)
# print(primes)

# Создайте пустые списки primes и not_primes.
# При помощи цикла for переберите список numbers.
# Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
# Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
# В процессе проверки на простоту записывайте числа из списка numbers в списки
# primes и not_primes в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
# Выведите списки primes и not_primes на экран(в консоль).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers)):
    if numbers[i] == 2 or numbers[i] == 3:
        primes.append(numbers[i])
    for j in range(2, numbers[i]):
        # is_prime = True
        if numbers[i] % j == 0:
            not_primes.append(numbers[i])
            # is_prime = False
            break
        elif numbers[i] % j != 0 and (numbers[i] + 1) % j != 0:
            primes.append(numbers[i])
            break


print(primes)
print(not_primes)


# то что должен выводить
# Primes: [2, 3, 5, 7, 11, 13]
# Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]
