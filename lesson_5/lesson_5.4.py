my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("lesson_5.4_text1.txt", "r", encoding="utf-8") as my_file:
    content = my_file.readlines()
    my_dict_new = {}
    my_list = []
    for line in content:
        a = line.index(" ")
        try:
            b = line.index("\n")
        except ValueError:
            b = len(line)
        my_dict_new.update({my_dict.get(line[:a]): line[a:b]})
    my_list = ["".join(item) for item in my_dict_new.items()]

with open("lesson_5.4_text2.txt", "a", encoding="utf-8") as my_file2:
    for i in my_list:
        print(i, file=my_file2)
