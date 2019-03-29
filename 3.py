# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

a = []

for i in range(20):
    a.append(randint(0, 20))
print(a)
a[a.index(max(a))], a[a.index(min(a))] = a[a.index(min(a))], a[a.index(max(a))]
print(a)