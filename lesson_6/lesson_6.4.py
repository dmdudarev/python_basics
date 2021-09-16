class Car:

    def __init__(self, s, c, n):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = False

    def go(self):
        print(f"{self.color} {self.name} поехала")

    def stop(self):
        print(f"{self.color} {self.name} остановилась")

    def turn(self, direction):
        print(f"{self.color} {self.name} повернула на{direction}")

    def show_speed(self):
        print(f"{self.color} {self.name} едет со скоростью {self.speed} км/ч")

    def siren(self):
        if self.is_police:
            print(f"{self.color} {self.name} включила сирену")
        else:
            print(f"{self.color} {self.name} включила сирену (водитель не полицейский и может лишиться прав)")


class TownCar(Car):

    def __init__(self, s, c, n):
        super().__init__(s, c, n)
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f"{self.color} {self.name} едет со скоростью {self.speed} км/ч (Вы превышаете разрешенную скорость!)")
        else:
            print(f"{self.color} {self.name} едет со скоростью {self.speed} км/ч")


class SportCar(Car):

    def __init__(self, s, c, n):
        super().__init__(s, c, n)
        self.is_police = False

    def show_speed(self):
        if self.speed > 200:
            print(f"{self.color} {self.name} едет со скоростью 200 км/ч (ограничено электроникой)")
        else:
            print(f"{self.color} {self.name} едет со скоростью {self.speed} км/ч")


class WorkCar(Car):

    def __init__(self, s, c, n):
        super().__init__(s, c, n)
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f"{self.color} {self.name} едет со скоростью {self.speed} км/ч (Вы превышаете разрешенную скорость!)")
        else:
            print(f"{self.color} {self.name} едет со скоростью {self.speed} км/ч")


class PoliceCar(Car):

    def __init__(self, s, c, n):
        super().__init__(s, c, n)
        self.is_police = True


a = TownCar(70, "красная", "Mazda")
a.go()
a.show_speed()
a.siren()
a.turn("лево")
a.stop()
print(f"{'*' * 70} ")
a1 = SportCar(250, "желтая", "Lamborghini")
a1.go()
a1.show_speed()
a1.turn("право")
a1.stop()
print(f"{'*' * 70} ")
b = WorkCar(50, "серая", "Renault")
b.go()
b.show_speed()
b.turn("лево")
b.stop()
print(f"{'*' * 70} ")
a = PoliceCar(70, "белая", "Skoda")
a.go()
a.show_speed()
a.siren()
a.turn("право")
a.stop()
