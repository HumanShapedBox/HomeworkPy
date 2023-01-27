# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета
# 385916 -> yes
# 123456 -> no

def happy_checker(number):
    count_left = 0
    count_right = 0
    while number > 999:
        count_right += number % 10
        number = number//10
    while number > 0:
        count_left += number % 10
        number = number//10
    if count_left == count_right:
        print('YES')
    else:
        print('NO')


ticket = int(input('Введите номер билета:'))
if 99999 < ticket < 1000000:
    happy_checker(ticket)
else:
    print('Номер билета должен содержать 6 цифр')
