a,b,c=map(int, input('Введите через пробел три разных числа: ').split())
while a==b or a==c or c==b:
    a, b, c = map(int, input('Числа должны быть разными! Попробуйте еще раз: ').split())

if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)