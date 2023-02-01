# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

import math

def searching_for_squarex(b, c):
    d = b*b + 4*c
    if d==0:
        x1 = int(b/2)
        x2 = 0
        return x1, x2
    elif d > 0: 
        x1 = int(b/2 + math.sqrt(d)/2)
        x2 = int(b/2 - math.sqrt(d)/2)
        return x1, x2
    else:
        x1, x2 = 0, 0
        return x1, x2

def perfect_match(b, x1, x2):
    y1 = 0
    if x1 !=0 and x2==0:
        y1 = b - x1
        return x1, y1
    elif x1 != 0 and x2 !=0:
        y1 = x2
        return x1, y1
    else:
        x1, y1 = 0, 0
        return x1, y1
    
s = int(input('Введите сумму загаданных чисел: '))
p = -int(input('Введите произведение загаданных чисел: '))
x, second_x = searching_for_squarex(s,p)
x, y = perfect_match(s, x, second_x)
if x !=0 and y!=0: print(f'Загаданные числа: {x, y}')
elif p == 0: print(f'Загаданные числа: {s}, 0')
else: print('Невозможно дать ответ по заданным параметрам')