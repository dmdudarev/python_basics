class ComplexNumber:
    def __init__(self, numb1, numb2):
        self.numb1 = int(numb1)
        self.numb2 = int(numb2)

    def __add__(self, other):
        self.result = (self.numb1 + other.numb1) + (self.numb2 + other.numb2) * 1j
        return self.result

    def __mul__(self, other):
        self.result = (self.numb1 * other.numb1 - self.numb2 * other.numb2) + (
                self.numb1 * other.numb2 + self.numb2 * other.numb1) * 1j
        return self.result


a = ComplexNumber(3, 4)
b = ComplexNumber(5, -2)
print(a + b)
print(a * b)
