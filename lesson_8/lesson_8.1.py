class Data:
    def __init__(self):
        pass

    @classmethod
    def numb(cls, my_data):
        my_list = my_data.split("-")
        day = int(my_list[0])
        month = int(my_list[1])
        year = int(my_list[2])
        return [day, month, year]

    @staticmethod
    def exam(data):

        if data[2] % 4 != 0:
            v = 0
        elif data[2] % 100 != 0:
            v = 1
        elif data[2] % 400 == 0:
            v = 1
        else:
            v = 0

        month_list = [1, 3, 5, 7, 8, 10, 12]
        
        if data[1] > 12 or data[1] < 1:
            n = "Неверно указан месяц"
        if data[0] > 31 or data[0] < 1:
            n = "Неверно указан день"
        elif month_list.count(data[1]) == 0 and data[0] > 30:
            n = "Неверно указан день"
        elif v == 0 and data[1] == 2 and data[0] > 28:
            n = "Неверно указан день"
        else:
            n = ".".join(map(str, data))
        return n


my_enter = input("Введите дату в формате день-месяц-год: ")
result = Data.exam(Data.numb(my_enter))
print(result)
