from math import factorial


def fact(n):
    for i in range(1, n + 1):
        result = factorial(i)
        yield result


try:
    n = int(input("Введите целое число больше нуля: "))
    for el in fact(n):
        print(el)
except ValueError:
    print("Неверный ввод")
