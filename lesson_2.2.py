my_enter = input("Введите числа через пробел: ")
my_list = my_enter.split()
l = len(my_list)
for i in range(0, l - 1, 2):
    i1 = my_list[i]
    i2 = my_list[i+1]
    my_list[i] = i2
    my_list[i+1] = i1
print(my_list)