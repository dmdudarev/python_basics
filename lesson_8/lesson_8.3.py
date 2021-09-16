class MyExeption(Exception):
    def __init__(self, text):
        self.text = text


my_list = []
while True:
    numb = input("Введите число: ")
    if numb == "stop":
        print(my_list)
        break
    try:
        if numb.isdigit() == 0:
            raise MyExeption("Вы ввели не число")
    except MyExeption as error:
        print(error)
    else:
        my_list.append(int(numb))
