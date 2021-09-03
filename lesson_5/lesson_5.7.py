from functools import reduce
from statistics import mean
from json import dump

my_string = "1234567890 "
my_dict = {}
av_profit_list = []
with open("lesson_5.7_text.txt", "r", encoding="utf-8") as my_file:
    content = my_file.readlines()
    for line in content:
        a = line.index(" ")
        my_list = [float(num) for num in (''.join(c for c in line if c in my_string)).split()]
        my_profit = reduce(lambda x, y: x - y, my_list)
        av_profit_list.append(my_list[0]) if my_profit >= 0 else av_profit_list
        my_dict.update({line[:a]: my_profit})
    average_profit = mean(av_profit_list)
    my_result = [my_dict, {'average_profit': average_profit}]
    print(my_result)
with open("lesson_5.7_json.json", "a", encoding="utf-8") as my_file2:
    dump(my_result, my_file2, indent=4, ensure_ascii=False)
