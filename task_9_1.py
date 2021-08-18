import time


class TrafficLight:
    def __init__(self):
        self.__color = "Red"

    def running(self):
        while True:
            print(f'{self.__color}, 7 sec')
            time.sleep(7)
            self.__color = "Yellow"
            print(f'{self.__color}, 2 sec')
            time.sleep(2)
            self.__color = "Green"
            print(f'{self.__color}, 10 sec')
            time.sleep(10)
            self.__color = "Red"


a = TrafficLight()
a.running()
