def my_func():
    my_list = []
    while True:
        my_enter = input("Введите числа через пробел (для выхода введите 'q'): ")
        my_enter2 = my_enter.replace(" ", "")
        my_list2 = my_enter.split()
        if my_enter2.isdigit():
            for i in my_list2:
                my_num = int(i)
                my_list.append(my_num)
                my_sum = sum(my_list)
            print(my_sum)
        else:
            try:
                m = my_list2.index("q")
                n = my_list2.count("q")
                for i in range(n):
                    my_list2.remove("q")
                    for i in my_list2:
                        my_num = int(i)
                        my_list.append(my_num)
                    my_sum = sum(my_list)
                    return my_sum
            except ValueError:
                print("Некорректный ввод")


print(my_func())
