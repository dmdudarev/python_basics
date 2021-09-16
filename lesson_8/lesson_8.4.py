class Warehouse:
    my_warehouse = []

    def __init__(self):
        self.device = {"название": "название", "свойства": "свойства"}

    def arrival(self, name, specific):
        self.device = {"название": name, "свойства": specific}
        Warehouse.my_warehouse.append(self.device)

    def departure(self, name, specific):
        self.device = {"название": name, "свойства": specific}
        Warehouse.my_warehouse.remove(self.device)


class OfficeEquipment:
    def __init__(self, name):
        self.name = name  # принтер, сканер, МФУ


class Printer(OfficeEquipment):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model  # цветной-ч/б
        self.name = "принтер"


class Scanner(OfficeEquipment):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model  # слайдер, планшет, комплекс
        self.name = "сканер"


class MFD(OfficeEquipment):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model  # наличие wi-fi
        self.name = "МФУ"


my_class = Warehouse()
while True:
    # вывод меню выбора операции
    print('Основное меню:\n1 - добавить устройство на склад, 2 - просмотреть все данные, '
          '3 - забрать устройство со склада, 0 - выход')

    my_cmd = int(input("Номер операции: "))
    if my_cmd == 0:  # выход из программы
        print('Работа завершена!')
        break
    elif my_cmd == 2:  # вывод всех позиций в списке
        for i in Warehouse.my_warehouse:
            print(i)
    elif my_cmd == 1:  # добавить на склад
        # w += 1
        a = int(input("Название (принтер (1), сканер (2), МФУ (3)): "))
        z = int(input("Свойство (принтер - цветной (1), ч/б (2); "
                      "сканер - слайдер (1), планшет (2), комплекс (3); МФУ - с wi-fi (1), без wi-fi (2)): "))
        x = ["Printer", "Scanner", "MFD"]
        y = [["цветной", "ч/б"], ["слайдер", "планшет", "комплекс"], ["с wi-fi", "без wi-fi"]]
        if a == 1:
            if z == 1 or z == 2:
                my_class1 = Printer(x[a - 1], y[a - 1][z - 1])
            else:
                print("Нет такой опции")
        elif a == 2:
            if z == 1 or z == 2 or z == 3:
                my_class1 = Scanner(x[a - 1], y[a - 1][z - 1])
            else:
                print("Нет такой опции")
        elif a == 3:
            if z == 1 or z == 2:
                my_class1 = MFD(x[a - 1], y[a - 1][z - 1])
            else:
                print("Нет такой опции")
        else:
            print("Нет такой опции")
        Warehouse.arrival(my_class, my_class1.name, my_class1.model)
        del my_class1
        for i in Warehouse.my_warehouse:
            print(i)
    elif my_cmd == 3:  # забрать со склада
        print("Какое устройство вам нужно?")
        a = int(input("Название (принтер (1), сканер (2), МФУ (3)): "))
        z = int(input("Свойство (принтер - цветной (1), ч/б (2); "
                      "сканер - слайдер (1), планшет (2), комплекс (3); МФУ - с wi-fi (1), без wi-fi (2)): "))
        x = ["Printer", "Scanner", "MFD"]
        y = [["цветной", "ч/б"], ["слайдер", "планшет", "комплекс"], ["с wi-fi", "без wi-fi"]]
        if a == 1:
            if z == 1 or z == 2:
                my_class1 = Printer(x[a - 1], y[a - 1][z - 1])
            else:
                print("Нет такой опции")
        elif a == 2:
            if z == 1 or z == 2 or z == 3:
                my_class1 = Scanner(x[a - 1], y[a - 1][z - 1])
            else:
                print("Нет такой опции")
        elif a == 3:
            if z == 1 or z == 2:
                my_class1 = MFD(x[a - 1], y[a - 1][z - 1])
            else:
                print("Нет такой опции")
        else:
            print("Нет такой опции")
        try:
            Warehouse.departure(my_class, my_class1.name, my_class1.model)
        except:
            print("На складе нет такого устройства")
        del my_class1
        for i in Warehouse.my_warehouse:
            print(i)
    else:
        print("Некорректная команда")
