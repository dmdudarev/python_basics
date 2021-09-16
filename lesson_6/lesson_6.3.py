class Worker:

    def __init__(self, n, s, p):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"wage": "wage", "bonus": "bonus"}


class Position(Worker):

    def __init__(self, n, s, p):
        super().__init__(n, s, p)

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self, v1, v2):
        self._income.update({"wage": v1, "bonus": v2})
        print(f"Доход: {float(self._income.get('wage')) + float(self._income.get('bonus')):.2f}")


a = Position("Ivan", "Ivanov", "Manager")
a.get_full_name()
a.get_total_income(10000, 2000)
