from time import sleep


class TrafficLight:
    color = ["green", "yellow", "red", "yellow", "green"]

    def running(self, repeat):
        self.repeat = repeat
        x = 1
        while x <= self.repeat:
            for i in self.color:
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
            x += 1


a = TrafficLight()
a.running(1)
