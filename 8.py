# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

n=int(input('Введите количество членов последовательности: '))
a=int(input('Введите искомую цифру: '))
s=0
for i in range(n):
    x=int(input('Введите член последовательности: '))
    if x == a:
        s+=1
print(s)

