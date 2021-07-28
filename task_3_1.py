translate_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                  'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять', 'zero': 'ноль'}


def num_translate():
    num_eng = input('Введите число от 0 до 10 на английском ')
    print(translate_dict.get(num_eng, 'перевод невозможен'))


num_translate()
