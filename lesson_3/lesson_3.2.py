def my_func(**kwargs):
    return ', '.join(kwargs.values())


print(my_func(nm=input("Введите Ваше имя: "), snm=input("Введите Вашу фамилию: "),
              byear=input("Введите Ваш год рождения: "), city=input("Введите Ваш город проживания: "),
              em=input("Введите Ваш e-mail: "), phnum=input("Введите Ваш номер телефона: ")))
