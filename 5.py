# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве
from random import random

s = []

for i in range(20):
    s.append(int(random() * 100) - 50)
print(s)

i = 0
index = -1
while i < 20:
    if s[i] < 0 and index == -1:
        index = i
    elif s[i] < 0 and s[i] > s[index]:
        index = i
    i += 1

print(index + 1, ':', s[index])