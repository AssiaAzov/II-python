import random

a1,a2 = map(int, input('Введите два числа через пробел: ').split())
n =  random.randint(a1,a2)
print(n)

a1,a2 = map(float, input('Введите два числа через пробел: ').split())
n = random.uniform(a1, a2)
print(round(n, 3))

a1,a2 = map(ord, input('Введите две буквы через пробел: ').split())
n = random.randint(a1,a2)
print(chr(n))