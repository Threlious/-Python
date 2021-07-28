def thesaurus(*args):
    name_dict = {}  # пустой словарь
    for name in args:  # перебираем значения имён в аргументах функции
        first_letter = name[0]  # первая буква = 0 индекс в аргументе
        if first_letter not in name_dict:  # если первой буквы аргумента еще нет в словаре
            name_dict[first_letter] = [name]
        else:
            name_dict[first_letter] += [name]
    return name_dict


print(thesaurus("Masha", "Tisha", "Seraphina", "Sophia"))
