# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
from random import randint

minimum = int(input('Укажите нижнюю границу значений: '))
maximum = int(input('Укажите верхнюю границу значений: '))
n = int(input('Укажите количество элементов: '))
my_list = [randint(1, 100) for i in range(n)]
ap_list = []
for i in range(len(my_list)):
    if minimum < my_list[i] < maximum:
        ap_list.append(i)
        i += 1
print(my_list)
print(f'Индексы элементов, удовлетворяющих условию: {ap_list}')