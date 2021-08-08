from json import dump
import itertools
with open("users.csv", "r", encoding="UTF-8") as users:
    with open("hobby.csv", "r", encoding="UTF-8") as hobby:
        if len(users.readlines()) >= len(hobby.readlines()):
            users.seek(0)
            hobby.seek(0)
            with open("comb.json", "w", encoding="UTF-8") as f:
                names_comb = itertools.zip_longest((" ".join(n.split(",")) for n in users), hobby)
                names_dict = {str(name).strip(): str(hobby).strip() for name, hobby in names_comb}
                dump(names_dict, f, ensure_ascii=False, indent=2)
            print(names_dict)
        else:
            exit(1)
