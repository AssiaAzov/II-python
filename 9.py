# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import random

x = 10
y = 5
a = []
for i in range(y):
    b = []
    for j in range(x):
        n = int(random() * 200)
        b.append(n)
        print('%4d' % n, end='')
    a.append(b)
    print()

mx = -1
for j in range(x):
    mn = 200
    for i in range(y):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("Максимальный среди минимальных: ", mx)