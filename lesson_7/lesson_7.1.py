from itertools import zip_longest


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            print("Размеры матриц разные, разница будет заполнена нулями")
        else:
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    print("Размеры матриц разные, разница будет заполнена нулями")
        result = []
        for x, y in zip_longest(self.matrix, other.matrix, fillvalue=[0]):
            result.append([a + b for a, b in zip_longest(x, y, fillvalue=0)])
        result_1 = [""]
        for x in result:
            for y in x:
                result_1.append(y)
            result_1.append("\n")
        return " ".join(map(str, result_1))

    def __str__(self):
        result_1 = [""]
        for x in self.matrix:
            for y in x:
                result_1.append(y)
            result_1.append("\n")
        return " ".join(map(str, result_1))


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix_1 + matrix_2)
