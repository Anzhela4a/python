from time import sleep

class TrafficLight:
    __color: str
    time: int

    def __init__(self, __color, time):
        self.__color = __color
        self.time = time

    def traffic_light_timer(self):
        print(self.__color)
        sleep(self.time)

red = TrafficLight('Red', 7)
yellow = TrafficLight('Yellow', 2)
green = TrafficLight('Green', 11)

while True:
    red.traffic_light_timer()
    yellow.traffic_light_timer()
    green.traffic_light_timer()

