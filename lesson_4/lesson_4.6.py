from itertools import count
from itertools import cycle

my_list = []

try:
    my_num = abs(int(input("Введите целое положительное число: ")))
    for num in count(my_num):
        if num > my_num + 10:
            break
        else:
            my_list.append(num)
except ValueError:
    print("Неверный ввод")

print(my_list)

try:
    my_num_f = abs(int(input("Введите количество повторов (целое положительное число): ")))
    c = 0
    for num_f in cycle(my_list):
        if c > my_num_f:
            break
        print(num_f)
        c += 1
except ValueError:
    print("Неверный ввод")
