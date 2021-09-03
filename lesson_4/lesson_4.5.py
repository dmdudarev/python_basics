from functools import reduce

my_list = [num for num in range(100, 1001) if num % 2 == 0]
result = reduce(lambda x, y: x * y, my_list)

print(result)
