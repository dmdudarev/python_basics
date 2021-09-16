class Cell:

    def __init__(self, cell):
        self.cell = int(cell)

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if (self.cell - other.cell) < 0:
            return "Отрицательное значение"
        else:
            return self.cell - other.cell

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        return int(self.cell // other.cell)

    def make_order(self, row):
        a = self.cell // row
        b = self.cell % row
        x = 1
        while x <= a:
            print(f"{'*' * row}")
            x += 1
        print(f"{'*' * b}")


cell_1 = Cell(12)
cell_2 = Cell(11)
cell_1.make_order(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
