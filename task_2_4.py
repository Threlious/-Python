initial_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор '
                                                                                                           'аэлита']
print(id(initial_list))
for idx in range(len(initial_list)):
    initial_list[idx] = initial_list[idx].split(" ")
    initial_list[idx] = initial_list[idx][-1].title()
for idx in range(len(initial_list)):
    print(f"Привет, {initial_list[idx]}")
print(id(initial_list))
