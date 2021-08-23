class Storage:
    def __init__(self):
        self.equipment_dict = {}  # в словаре хранится информация о марках оборудования и связыннх с ним характеристиках
        self.storage_dict = {"Printer": 0, "Scanner": 0, "Xerox": 0}  # в словаре хранится количество оборудования по
        # типам

    def get_equipment(self, type_eq):  # передача оборудования на склад
        if type_eq == "printer":
            self.storage_dict["Printer"] += 1
        if type_eq == "scanner":
            self.storage_dict["Scanner"] += 1
        if type_eq == "xerox":
            self.storage_dict["Xerox"] += 1

    def move(self, other, name):  # удаление с исходного и перемещение на другой склад, в программе предполагается,
        # что склада всего два
        if name in self.equipment_dict:
            value = self.equipment_dict[name]
            self.storage_dict[self.equipment_dict[name]["Title"]] -= 1
            self.equipment_dict.pop(name)
            other.equipment_dict[name] = value


class WrongValue(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipment:
    def __init__(self):
        self.service_time = int(input("Enter service time of equipment "))
        self.quality = input("Enter equipment quality (good, bad, broken): ")


class Printer(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.type = input("Enter type of printer (1 - laser, 2 - solid ink): ")
        self.title = "Printer"
        self.name = None
        if self.type == str(1):
            self.type = "Laser"
        if self.type == str(2):
            self.type = "Solid ink"


class Scanner(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.type = input("Enter type of scanner (1 - automated, 2 - handheld): ")
        self.title = "Scanner"
        self.name = None
        if self.type == str(1):
            self.type = "Automated"
        if self.type == str(2):
            self.type = "Handheld"


class Xerox(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.type = input("Enter type of scanner (1 - black n white, 2 - colour): ")
        self.title = "Xerox"
        self.name = None
        if self.type == str(1):
            self.type = "Black-and-white"
        if self.type == str(2):
            self.type = "Colour"


#  Меню


storage = Storage()
final_storage = Storage()
while True:
    try:
        ch1 = int(input("What do you want?\n1 - make new equipment\n2 - move item\n"
                        "3 - show equipment info\n"
                        "4 - show storage info\n5 - Exit\n"))  # вводится, что хочет
        # пользователь
        if ch1 not in range(1, 6):
            raise WrongValue("Wrong value")
    except (WrongValue, ValueError) as err:
        print(err)
    else:
        if ch1 == 1:  # передача оборудования на склад
            ch2 = int(input("What type of equipment?\n1 - printer\n2 - scanner\n3 - xerox\n"))
            if ch2 == 1:
                printer = Printer()
                try:
                    if printer.type != "Laser" and printer.type != "Solid ink":
                        raise WrongValue("Wrong value")
                except WrongValue as err:
                    print(err)
                else:
                    storage.get_equipment("printer")
                    printer.name = input("Enter printer name: ")
                    storage.equipment_dict[printer.name] = {"Title": printer.title, "Printer type": printer.type,
                                                            "Service time": printer.service_time,
                                                            "Quality": printer.quality}
            if ch2 == 2:
                scanner = Scanner()
                try:
                    if scanner.type != "Automated" and scanner.type != "Handheld":
                        raise WrongValue("Wrong value")
                except WrongValue as err:
                    print(err)
                else:
                    storage.get_equipment("scanner")
                    scanner.name = input("Enter scanner name: ")
                    storage.equipment_dict[scanner.name] = {"Title": scanner.title, "Scanner type": scanner.type,
                                                            "Service time": scanner.service_time,
                                                            "Quality": scanner.quality}
            if ch2 == 3:
                xerox = Xerox()
                try:
                    if xerox.type != "Black-and-white" and xerox.type != "Colour":
                        raise WrongValue("Wrong value")
                except WrongValue as err:
                    print(err)
                else:
                    storage.get_equipment("xerox")
                    xerox.name = input("Enter xerox name: ")
                    storage.equipment_dict[xerox.name] = {"Title": xerox.title, "Xerox type": xerox.type,
                                                          "Service time": xerox.service_time,
                                                          "Quality": xerox.quality}
        if ch1 == 2:
            popped = input("Enter item to remove ")
            storage.move(final_storage, popped)
        if ch1 == 3:  # марки оборудования
            print(f'{storage.equipment_dict}\n')
        if ch1 == 4:  # склад
            print(f'{storage.storage_dict}\n')
        if ch1 == 5:  # выход
            print("bb")
            break
