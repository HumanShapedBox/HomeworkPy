# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел A i. 
# Последняя строка содержит число X

from random import randint

n = int(input('Укажите желаемую длинну массива: '))
if n > 0: numbers = [randint(1, 10) for i in range(n)]
else: n = int(input('Требуется целое положительное число (например, 5): '))
x = int(input('Введите число, близкие элементы которому будем искать: '))
diff = abs(x - numbers[0])
closest_element = numbers[0]
for i in range(1, len(numbers)):
    if x == numbers[i]:
        closest_element = numbers[i]
        break
    elif abs((x - numbers[i])) < diff:
        diff = abs(x - numbers[i])
        closest_element = numbers[i]
    i +=1
print(numbers)
print(f'Самый близкий по величине к {x} элемент в массиве: {closest_element}')