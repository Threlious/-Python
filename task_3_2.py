translate_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                  'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять', 'zero': 'ноль'}


def num_translate_adv():
    num_eng = input('Введите число от 0 до 10 на английском ')
    if num_eng.islower():
        print(translate_dict.get(num_eng))
    elif num_eng.istitle():
        print(str(translate_dict.get(num_eng.lower())).title())


num_translate_adv()
