class ZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    x = int(input("Enter divisible "))
    y = int(input("Enter divisor "))
    if y == 0:
        raise ZeroDivision("Could not be 'zero'")
except (ValueError, ZeroDivision) as err:
    print(err)
else:
    print(x / y)