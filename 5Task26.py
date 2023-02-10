# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии

def expo (n, m):
     if m == 1:
         return n
     return expo(n, m-1) * n

a = int(input('Введите число: '))
b = int(input('Введите степень: '))
a_expo = expo(a, b)
print(a_expo)