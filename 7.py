a,b,c=map(int, input('Введите через пробел длины сторон: ').split())
if a+b>c and a+c>b and b+c>a:
    print('существует')
    if a != b and a != c and b != c:
        print("Разносторонний")
    elif a == b == c:
        print("Равносторонний")
    else:
        print("Равнобедренный")
else:
    print('не существует')
