def int_func():
    my_enter = input("Введите слово маленькими латинскими буквами (другие символы будут удалены): ")
    my_string = "qwertyuiopasdfghjklzxcvbnm"
    my_result = (''.join(c for c in my_enter if c in my_string)).title()
    return (my_result)


print(int_func())
