a,b = map(ord, input('Введите две буквы через пробел: ').split())
a = a - ord('a') + 1
b = b - ord('a') + 1
print(f"Позиции букв: {a} и {b}")
print('Между буквами символов:', abs(a - b) - 1)

