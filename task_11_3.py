class ListIsdigit(Exception):
    def __init__(self, txt):
        self.txt = txt


user_list = []
while True:
    user_list.append(input("Enter number "))
    if user_list[-1] == "stop":
        user_list.pop()
        break
try:
    for i in user_list:
        if not i.isdigit():
            raise ListIsdigit("At least one value is not digit")
except ListIsdigit as err:
    print(err)
    print(user_list)
else:
    print("All data is correct")
    new_list = list(map(int, user_list))
    print(new_list)
