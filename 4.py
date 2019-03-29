# Определить, какое число в массиве встречается чаще всего.

from random import randint

s = []

for i in range(20):
    s.append(randint(0, 20))
print(s)

max = s[0]
max_count = s.count(max)
for el in s:
     if s.count(el)>max_count:
         max = el
         max_count = s.count(el)
print(max)
