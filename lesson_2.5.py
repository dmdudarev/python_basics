my_list = [7, 5, 3, 3, 2]
my_enter = input("Введите натуральное число: ")
while not my_enter.isdigit():
    my_enter = input("Нужно ввести только натуральное число: ")

my_number = int(my_enter)
if my_list[-1] > my_number:
    my_list.append(my_number)
else:
    for i in my_list:
        if my_number >= i:
            my_list.insert(my_list.index(i), my_number)
            break
print("*" * 60)
print(my_list)
print("*" * 60)
