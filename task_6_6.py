from sys import argv
with open("bakery.csv", "a", encoding="utf-8") as bake_a:
    with open("bakery.csv", "r", encoding="utf-8") as bake_r:
        if len(argv) > 1 and [i for i in argv[1:] if i.replace(".", "").isdigit() or i.replace(",", "").isdigit()]:
            if len(argv) == 3:
                start, finish = map(int, argv[1:])
                print(*(v for i, v in enumerate(bake_r) if start - 1 <= i < finish))
            if "," in argv[1] or "." in argv[1]:
                print(f'{float(argv[1].replace(",", "."))}', file=bake_a)
            else:
                print(*(v for i, v in enumerate(bake_r) if i >= int(argv[1]) - 1))
        else:
            print(bake_r.read())
