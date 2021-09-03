with open("lesson_5.1_text.txt", 'a') as my_file:
    my_text = 1
    while my_text:
        my_text = input("Введите данные: ")
        print(f"{my_text}", file=my_file)
