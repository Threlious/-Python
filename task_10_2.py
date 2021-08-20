from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def consumption(self):
        value = self.size / 6.5 + 0.5
        return value


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def consumption(self):
        value = 2 * self.height + 0.3
        return value


coat = Coat(1)
print(coat.consumption)
costume = Costume(1)
print(costume.consumption)
print(coat.consumption + costume.consumption)
