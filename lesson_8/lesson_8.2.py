class MyExeption(Exception):
    def __init__(self, text):
        self.text = text


numb1 = input("Введите делимое: ")
numb2 = input("Введите делитель: ")
try:
    numb1 = int(numb1)
    numb2 = int(numb2)
    if numb2 == 0:
        raise MyExeption("Нельзя делить на нуль")
except (ValueError, MyExeption) as error:
    print(error)
else:
    print(numb1 / numb2)
