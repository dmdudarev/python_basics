first_result = int(input("Введите Ваш начальный результат (км): "))
final_result = int(input("Введите Ваш желаемый результат (км): "))
progress = 1.1

# progress = int(input("Введите Ваш ожидаемый ежедневный прирост (%): ")) / 100 + 1

day = 1

result = first_result

while result // final_result < 1:
    result = result * progress
    day += 1

print(
    f"При данной интенсивности тренировок Вы достигните желаемого результата (не менее {final_result} км) за {day} дней")
