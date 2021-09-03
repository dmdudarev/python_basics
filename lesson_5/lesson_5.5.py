from random import randint

with open("lesson_5.5_text.txt", "a+", encoding="utf-8") as my_file:
    print(" ".join([str(randint(-100, 100)) for _ in range(20)]), file=my_file)
    my_file.seek(0, 0)
    my_list = [int(num) for num in my_file.readlines()[0].split()]
    print(f"Создан набор чисел:\n{my_list}\n"
          f"Сумма чисел: {sum(my_list)}"
          )
