class Stationery:
    def __init__(self):
        self.title = None

    def draw(self):
        print("Drawing starts")


class Pen(Stationery):
    def draw(self):
        self.title = "Pen"
        print(f'{self.title} is selected')


class Pencil(Stationery):
    def draw(self):
        self.title = "Pencil"
        print(f'{self.title} is selected')


class Handle(Stationery):
    def draw(self):
        self.title = "Handle"
        print(f'{self.title} is selected')


stationery = Stationery()
stationery.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
