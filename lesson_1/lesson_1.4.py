number = int(input("Введите целое положительное число: "))
max_number = 0

while number > 0:
    number_x = number % 10
    if number_x > max_number:
        max_number = number_x
    number = number // 10

print(f"Наибольшая цифра в числе: {max_number}")
