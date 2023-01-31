# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
#
# 5 -> 1 0 1 1 0
# 2

import random
coins = int(input('Укажите количество монет: '))
if coins <= 1: 
    coins = int(input('Нечего переворачивать. Введите число больше одного: '))
heads = tails = 0
for i in range(coins):
    pos = random.randint(0, 1)
    print(pos, end=' ')
    if pos == 0:
        tails += 1
    else:
        heads += 1
print()
if heads < tails:
    print(f'Минимум нужно перевернуть {heads}')
else:
    print(f'Минимум нужно перевернуть {tails}')