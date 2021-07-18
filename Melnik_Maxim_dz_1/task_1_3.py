number = int(input("Введите число для склонения слова 'Процент': "))
if number == 1:
    print(str(number) + ' процент')
elif 1 < number < 5:
    print(str(number) + ' процента')
elif 4 < number < 21:
    print(str(number) + ' процентов')
else:
    print('Введено число больше 20')
print('1 процент')
x = 2  # блок чисел с окончанием "а"
while x < 5:
    print(str(x) + ' процента')
    x += 1
y = 5  # блок чисел с окончанием "ов"
while y < 21:
    print(str(y) + ' процентов')
    y += 1
