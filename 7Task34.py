# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод: Парам пам-пам

poem = input('Стихотворение Винни: ').lower().replace('-', '').split(' ')
only_vowels = []
for i in range(len(poem)):
    only_vowels.append(list(filter(lambda i: i in 'уеэоаыяиюё', poem[i])))
flag = True
for i in range(len(only_vowels) - 1):
    if len(only_vowels[i]) != len(only_vowels[i+1]):
        flag = False
        break
print('Парам пам-пам' if flag == True else 'Пам парам')