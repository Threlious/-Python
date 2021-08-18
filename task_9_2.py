class Road:
    def __init__(self):
        self._length = 20
        self._width = 5000

    def road_mass(self):
        mass = int(self._length * self._width * 25 * 5 / 1000)
        return mass


a = Road()
print(a.road_mass())
