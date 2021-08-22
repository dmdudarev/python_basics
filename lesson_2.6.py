my_list = [(1, {'название': 'ноутбук', 'цена': '40000', 'количество': '1', 'ед': 'шт.'})]  # исходный список
while True:
    # вывод меню выбора операции
    print(
        f"{'*' * 76}\n"
        f"{'*' * 3:<32}{'Основное меню:':<41}{'*' * 3}\n"
        f"{'*' * 3} (1 - новый товар, 2 - просмотреть все данные, 3 - анализ, 0 - выход) {'*' * 3}\n"
        f"{'*' * 76}"
    )
    my_cmd = int(input("Номер операции: "))
    if my_cmd == 0:  # выход из программы
        print(
            f"{'*' * 76}\n"
            f"{'*' * 3:<31}{'Работа завершена!':<42}{'*' * 3}\n"
            f"{'*' * 76}"
        )
        break
    elif my_cmd == 1:  # ввод параметров новой позиции в список
        number = int(len(my_list)) + 1
        my_input1 = input("Новый товар. Название: ")
        my_input2 = input("Новый товар. Цена: ")
        my_input3 = input("Новый товар. Количество: ")
        my_input4 = input("Новый товар. Единицы измерения товара: ")
        my_dict = dict(название=my_input1, цена=my_input2, количество=my_input3, ед=my_input4)
        my_tuple = (number, my_dict)
        my_list.append(my_tuple)
        print(
            f"{'*' * 76}\n"
            f"Добавлено: {my_tuple}"
        )
    elif my_cmd == 2:  # вывод всех позиций в списке
        for i in my_list:
            print(
                f"{'*' * 76}"
                f"{i}"
            )
    elif my_cmd == 3:  # анализ списка по пунктам
        analisys_list = []
        while True:
            print(
                f"{'*' * 76}\n"
                f"{'*' * 3:<32}{'Меню анализа:':<41}{'*' * 3}\n"
                f"{'*' * 3:<6}(1 - название, 2 - цена, 3 - количество, 4 - единицы, 0 - выход){'*' * 3:>6}\n"
                f"{'*' * 76}"
            )
            my_cmd2 = int(input("Номер операции: "))
            if my_cmd2 == 0:  # выход из анализа
                print(
                    f"{'*' * 76}\n"
                    f"{'*' * 3:<30} Анализ завершен! {'*' * 3:>28}\n"
                    f"{'*' * 76}"
                )
                break
            elif my_cmd2 == 1:  # анализ по названию, только уникальные названия
                for i in my_list:
                    analisys_list.append(i[1].get("название"))
                analisys_set = set(analisys_list)
                print(f"Название: {analisys_set}")
            elif my_cmd2 == 2:  # анализ по цене
                for i in my_list:
                    analisys_list.append(i[1].get("цена"))
                print(f"Цена: {analisys_list}")
            elif my_cmd2 == 3:  # анализ по количеству
                for i in my_list:
                    analisys_list.append(i[1].get("количество"))
                print(f"Количество: {analisys_list}")
            elif my_cmd2 == 4:  # анализ по единицам, только уникальные единицы
                for i in my_list:
                    analisys_list.append(i[1].get("ед"))
                analisys_set = set(analisys_list)
                print(f"Единицы: {analisys_set}")
            else:  # сообщение, если выбран номер не из списка операций анализа
                print("*" * 30)
                print("*** Некорректная операция! ***")
    else:  # сообщение, если выбран номер не из списка операций
        print("*" * 30)
        print("*** Некорректная операция! ***")
