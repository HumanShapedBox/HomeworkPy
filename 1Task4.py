# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
#
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

s = int(input('Общее количество журавликов: '))
if s%6==0:
    boys_cranes = s // 6
    kate_cranes = boys_cranes * 4
    print(f'Петя - {boys_cranes}, Катя - {kate_cranes}, Серёжа - {boys_cranes}')
else: print('Часть журавликов потерялась - невозможно распределить поделки согласно условию задачи')