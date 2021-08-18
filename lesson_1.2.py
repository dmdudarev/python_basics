tm_sec = int(input("Введите время в секундах: "))
hour = tm_sec // 3600
minut = (tm_sec % 3600) // 60
sec = (tm_sec % 3600) % 60
print (f"{hour:02}:{minut:02}:{sec:02}")
