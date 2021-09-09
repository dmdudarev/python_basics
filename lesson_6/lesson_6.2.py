class Road:

    def __init__(self, l, w):
        self._length = l
        self._width = w

    def massa(self, massa1, thickness):
        result = (self._length * self._width * massa1 * thickness) / 1000
        print(f"Для покрытия дорожного полотна необходимо {result} т. асфальта")


a = Road(5000, 20)
a.massa(25, 5)
