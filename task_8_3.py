def type_logger(func):  # декоратор, где аргумент - это основная функция
    def type_wrapper(*args):  # функция в декортаторе, где аргументы - это аргументы в основной функции
        for i in args:
            print(f'{i}: {type(i)}', end=", " if args.index(i) < len(args) - 1 else "")
        return func
    return type_wrapper


@type_logger
def calc_cube(*args):
    for i in args:
        return i ** 3


a = calc_cube(7, "Hello", None, {5: 8})
