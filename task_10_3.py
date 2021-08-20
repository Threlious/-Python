class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'Рещультирующая клетка с количеством ячеек {self.quantity}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return Cell(self.quantity - other.quantity)
        else:
            raise SyntaxError("Wrong sub")

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __floordiv__(self, other):
        if self.quantity >= other.quantity:
            return Cell(self.quantity // other.quantity)
        else:
            raise SyntaxError("Wrong floordiv")

    def make_order(self, row_quantity):
        return "\n".join("*" * row_quantity for i in range(self.quantity // row_quantity)) \
               + "\n" + "*" * (self.quantity % row_quantity)


cell_1 = Cell(7)
cell_2 = Cell(4)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(2))
