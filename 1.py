# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

import timeit
import cProfile

#function calls in 20.254 seconds
def a():
    a = input("Введите число: ")
    b = input("Введите искомую цифру: ")
    x = 0
    for i in a:
        if i == b:
            x += 1
    print(x)


cProfile.run("a()")


# function calls in 4.641 seconds
def b():
    a = input("Введите число: ")
    b = input("Введите искомую цифру: ")
    x = []
    for i in a:
        if i == b:
            x.append(i)
    print(x.count(b))


cProfile.run("b()")

