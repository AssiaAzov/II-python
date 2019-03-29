# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

from random import random
n = 10
a = [0]*n
x = []
for i in range(n):
    a[i] = int(random() * 10) + 10
    if a[i] % 2 == 0:
        x.append(i)
print(a)
print('Индексы четных элементов: ', x)