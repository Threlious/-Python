from functools import wraps


def val_checker(lambda_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(num):
            if lambda_func(num):
                print(func(num))
            else:
                raise ValueError("Wrong value")
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    a = calc_cube(5)
except (ValueError, TypeError) as err:
    print(err)
