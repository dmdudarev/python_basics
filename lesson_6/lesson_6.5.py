class Stationery:

    def __init__(self, t):
        self.title = t  # марка предмета

    def draw(self):
        print(f"Запуск отрисовки с помощью {self.title}.")


class Pen(Stationery):

    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        print(f"Запуск отрисовки с помощью ручки {self.title}.")


class Pencil(Stationery):

    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        print(f"Запуск отрисовки с помощью карандаша {self.title}.")


class Handle(Stationery):

    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        print(f"Запуск отрисовки с помощью маркера {self.title}.")


a = Pen('"Parker"')
a.draw()
b = Pencil('"Koh-i-noor"')
b.draw()
c = Handle('"Touch Twin"')
c.draw()
