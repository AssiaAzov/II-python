a=list((input('Введите трехзначное число ')))
while len(a) !=3:
    a=input('Трехзначное! Попробуйте еще раз:')

print(sum(map(int, a)))

print(int(a[0])*int(a[1]) + int(a[2]))
