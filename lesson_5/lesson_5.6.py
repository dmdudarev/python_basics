with open("lesson_5.6_text.txt", "r", encoding="utf-8") as my_file:
    content = my_file.readlines()
    my_list = []
    my_list2 = []
    for line in content:
        a = line.index(":")
        b = line.count("(")
        c = line.count(" ")
        # try:
        #     b = line.index("\n")
        # except ValueError:
        #     b = len(line)
        my_list.append(line[:a])
        # for i in range(b):
        #     my_list2.append(line[c:b])



        print(b)
