from random import randint


class Car:
    def __init__(self):
        self.speed = randint(40, 100)
        self.color = input("Enter car color ")
        self.name = input("Enter car name: ")
        police = randint(0, 1)
        self.is_police = None
        if police == 1:
            var = self.is_police = True
        else:
            var = self.is_police = False

    def show_speed(self):
        print(f'Current speed: {self.speed}')

    def go(self):
        print("Car goes")

    def stop(self):
        print("Car has stopped")

    def turn(self, direction):
        print(f'Car has turned {direction}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Current speed: {self.speed}')
            print("Speed is too high")
        else:
            print(f'Current speed: {self.speed}')
            print("Speed is OK")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Current speed: {self.speed}')
            print("Speed is too high")
        else:
            print(f'Current speed: {self.speed}')
            print("Speed is OK")


class SportCar(Car):
    def show_speed(self):
        if self.speed < 60:
            print(f'Current speed: {self.speed}')
            print("Speed is too low")
        else:
            print(f'Current speed: {self.speed}')
            print("Speed is OK")


class PoliceCar(Car):
    def show_speed(self):
        print(f'Current speed: {self.speed}')
        print(f'Car is police: {self.is_police}')


Town = TownCar()
Town.show_speed()
Work = WorkCar()
Work.show_speed()
Sport = SportCar()
Sport.show_speed()
Police = PoliceCar()
Police.show_speed()
