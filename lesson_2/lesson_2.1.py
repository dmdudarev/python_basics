my_list = [3, 5.6, "abc", True, None, [1, 2, 3], (4, 5), {8, 9}, {"k1": 32, "k2": 55},
           frozenset('abc'), bytes('ert', encoding='utf-8'), bytearray(b"rty"), ZeroDivisionError]

for i in my_list:
    print(type(i))
