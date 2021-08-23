class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f'Real part: {self.real} Imaginary part: {self.imaginary}i'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real + (-1 * self.imaginary * other.imaginary),  # real part
                             self.imaginary * other.real + self.real * other.imaginary)  # imaginary part


a = ComplexNumber(-2, 6)
b = ComplexNumber(7, -15)
print(f'Number a: {a}')
print(f'Number b: {b}')
print(f'Add: {a + b}')
print(f'Mul: {a * b}')
