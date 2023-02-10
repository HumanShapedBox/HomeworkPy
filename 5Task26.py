# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии

def expo (n, m):
    if m < 0:
        m *= -1
    if m == 1:
        return n
    return expo(n, m-1) * n

a = int(input('Введите число: '))
b = int(input('Введите степень: '))
a_expo = expo(a, b)
if a > 0 and b > 0:
    print(a_expo)
elif a > 0 and b < 0:
    print(1 / a_expo)
elif a < 0 and b > 0 and b % 2 == 0:
    print(a_expo * -1)
elif a < 0 and b < 0:
    if b % 2 == 0:
        print(-1 / a_expo)
    else:
        print(1 / a_expo)
elif b == 0 and a !=0:
    print(1)
elif a == 0 and b !=0:
    print(0)
else:
    print('Выражение не имеет смысла')