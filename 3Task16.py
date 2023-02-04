# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел A i. Последняя строка содержит число X

from random import randint

n = int(input('Укажите желаемую длинну массива: '))
if n > 0: mumbo_jumbo_list = [randint(1, 10) for i in range(n)]
else: n = int(input('Требуется целое положительное число (например, 5): '))
x = int(input('Какое число будем искать: '))
count = 0
for i in range(0, len(mumbo_jumbo_list)):
    if mumbo_jumbo_list[i] == x: count += 1
    i += 1

print(mumbo_jumbo_list)
print(f'Число {x} встречается {count} раз')