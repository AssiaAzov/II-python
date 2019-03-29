# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import random

n = 10
a = [0]*n
for i in range(n):
    a[i] = int(random()*50)
    print('%3d' % a[i], end='')
print()

min, max = 0, 0
for i in range(1, len(a)) :
    if a[i] > a[max] : max = i
    if a[i] < a[min] : min = i
if min < max :
    print(sum(a[min + 1 : max]))
else :
    print(sum(a[max + 1 : min]))
