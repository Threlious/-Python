class Worker:
    def __init__(self):
        self.name = input("Enter name ")
        self.surname = input("Enter surname ")
        self.position = input("Enter position ")
        self._income = {"wage": input("Enter wage "), "bonus": input("Enter bonus ")}


class Position(Worker):
    def get_full_name(self):
        print(f'Full name: {" ".join([self.name, self.surname])}')

    def get_total_income(self):
        total_income = int(self._income["wage"]) + int(self._income["bonus"])
        return total_income


a = Position()
print(f'Name: {a.name}')
print(f'Surname: {a.surname}')
print(f'Position: {a.position}')
a.get_full_name()
print(f'Total income: {a.get_total_income()}')
