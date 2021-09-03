from statistics import mean

with open("lesson_5.3_text.txt", "r", encoding="utf-8") as my_file:
    content = my_file.readlines()
    count_lines = len(content)
    my_dict = {}
    for line in content:
        a = line.index(" ")
        try:
            b = line.index("\n")
        except ValueError:
            b = len(line)
        my_dict.update({line[:a]: float(line[a:b])})
    my_list = [key for key, value in my_dict.items() if value < 20000.00]
    av_salary = mean(my_dict.values())
    print(f"Оклад менее 20000.00 у сотрудников:\n{my_list}")
    print(f"Средний оклад: {av_salary:.2f}")
