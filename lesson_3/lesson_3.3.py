def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    min_num = min(my_list)
    my_list.remove(min_num)
    result = sum(my_list)
    return result


print(my_func(5, 2, 3))
