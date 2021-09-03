def my_func(x, y):
    result = abs(x) ** round(-abs(y))
    return result


def my_func_2(x, y):
    num_1 = abs(x)
    num_2 = round(abs(y))
    num_3 = 1
    i = 1
    while i <= num_2:
        num_3 = num_3 * num_1
        i += 1
    result = 1 / num_3
    return result


print(f"Вариант 1: {my_func(10, -2)} (оператор **)\nВариант 2: {my_func_2(10, -2)} (цикл)")
