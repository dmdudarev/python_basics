from time import sleep
from sys import exit


class TrafficLight:

    def __init__(self, color):
        self.color = color
        self.color_list = ["green", "yellow", "red", "yellow"]

        if self.color_list.count(self.color) == 0:
            print("Неверный цвет! Возможные варианты: 'green', 'yellow', 'red'")
            exit()

    def running(self, repeat):
        self.repeat = repeat
        self.my_start = self.color_list.index(self.color)
        self.my_list = []
        for z in range(self.my_start, self.repeat + self.my_start):
            if z % 4 == 0:
                self.my_list.append(self.color_list[0])
            elif z > 4:
                self.my_list.append(self.color_list[z % 4])
            else:
                self.my_list.append(self.color_list[z])
        for i in self.my_list:
            if i == "green":
                print(f"\033[30m(*)"
                      f"\033[30m(*)"
                      f"\033[32m(*)"
                      f"\033[0m", end=''
                      )
                sleep(7)
                print(f"\r", end='')
            elif i == "yellow":
                print(f"\033[30m(*)"
                      f"\033[33m(*)"
                      f"\033[30m(*)"
                      f"\033[0m", end=''
                      )
                sleep(2)
                print(f"\r", end='')
            elif i == "red":
                print(f"\033[31m(*)"
                      f"\033[30m(*)"
                      f"\033[30m(*)"
                      f"\033[0m", end=''
                      )
                sleep(7)
                print(f"\r", end='')


a = TrafficLight("red")
a.running(5)
