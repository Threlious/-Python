from requests import get, utils


def currency_rates(code):
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    code = code.upper()
    if content.find(code) != -1 and len(code) == 3:  # проверка на соответствие кода html файлу и наличие 3 символов
        print(f'{content[content.find("Date"):content.find("Date") + 17]}')  # вывод времени
        code_str = content[content.find(code):]  # строка с информацие о валюте до конца html файла
        nominal = int(code_str[code_str.find("<Nominal>") + 9:code_str.find("</Nominal>")])  # номинал валюты
        rate = code_str[code_str.find("<Value>") + 7:code_str.find("</Value>")]  # курс валюты
        return f'{float(rate.replace(",", ".")) / nominal}'  # деление курса на номинал


print(currency_rates("USD"))
print(currency_rates("eur"))
