import re


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date(cls, date):
        d = date[0:2]
        m = date[3:5]
        y = date[-4:]
        if d.isdigit() and m.isdigit() and y.isdigit():
            print(f'day: {int(d)} month: {int(m)}  year: {int(y)}')
        else:
            raise ValueError("Wrong date format")

    @staticmethod
    def valid_date(date):
        re_date = re.compile(r'^(?:0[1-9]|[1-2][0-9]|3[0-1])-(?:0[1-9]|1[0-2])-20(?:0[0-9]|1[0-9]|2[01])$')  # years
        # in range 2000 - 2021
        assert re_date.match(date), f"wrong date format {date}"
        print("Right format")


a = Date
a.get_date("22-08-2021")
a.valid_date("22-12-2021")
