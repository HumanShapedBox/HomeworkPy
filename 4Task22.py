# Даны два неупорядоченных набора целых чисел (может быть, с # повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input('Сколько элементов будет в первом множестве: '))
m = int(input('Сколько элементов будет во втором множестве: '))
n_set = set()
for i in range(n): n_set.add(input('Введите элементы первого множества: '))
m_set = set()
for i in range(m): m_set.add(input('Введите элементы второго множества: '))
uniq_set = sorted(n_set | m_set)
print(uniq_set)