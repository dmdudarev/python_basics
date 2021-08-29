my_enter = input("Введите данные через пробел: ")
my_list = my_enter.split()
l = len(my_list)
for i in range(0, l):
    print(f"{i + 1}. {my_list[i][:10]}")
