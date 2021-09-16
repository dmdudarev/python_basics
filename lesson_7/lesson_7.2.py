from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param_1):
        self.param_1 = param_1

    @abstractmethod
    def sum_cloth(self):
        pass


class Coat(Clothes):
    def __init__(self, param_1):
        self.param_1 = param_1

    @property
    def sum_cloth(self):
        return f"{self.param_1 / 6.5 + 0.5:.2f}"


class Suit(Clothes):
    def __init__(self, param_1):
        self.param_1 = param_1

    @property
    def sum_cloth(self):
        return 2 * self.param_1 + 0.3


cl_1 = Coat(50)
cl_2 = Suit(1.82)
print(cl_1.sum_cloth)
print(cl_2.sum_cloth)
