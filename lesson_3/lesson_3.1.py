def my_function():
    try:
        num_1 = float(input("Введите первый аргумент (число): "))
        num_2 = float(input("Введите второй аргумент (число): "))
        result = num_1 / num_2
    except ZeroDivisionError:
        return "На нуль делить нельзя!"
    return result


my_result = my_function()
print(my_result)
