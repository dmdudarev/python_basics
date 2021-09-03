def int_func(my_enter):
    my_string = "qwertyuiopasdfghjklzxcvbnm"
    my_result = (''.join(c for c in my_enter if c in my_string)).title()
    return (my_result)


my_enter2 = input("Введите фразу маленькими латинскими буквами (другие символы будут удалены): ")
my_list = my_enter2.split()
for index, item in enumerate(my_list):
    my_list[index] = int_func(item)

print(' '.join(my_list))
