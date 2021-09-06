with open("lesson_5.2_text.txt", "r", encoding="utf-8") as my_file:
    content = my_file.readlines()
    count_lines = len(content)
    print(f"Количество строк в файле: {count_lines}")
    i = 1
    for line in content:
        count_word = len(line.split())
        print(f"Количество слов в строке {i}: {count_word}")
        i += 1
