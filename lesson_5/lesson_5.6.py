with open("lesson_5.6_text.txt", "r", encoding="utf-8") as my_file:
    content = my_file.readlines()
    my_dict = {}
    my_string = "1234567890 "
    for line in content:
        a = line.index(":")
        my_list = (''.join(c for c in line if c in my_string)).split()
        my_sum = sum([int(num) for num in my_list])
        my_dict.update({line[:a]: my_sum})
    print(my_dict)
