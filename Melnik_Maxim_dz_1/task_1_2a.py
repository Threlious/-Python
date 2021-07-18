checklist = [1]  # массив с первым элементом
idx = 0  # индекс для массива
while checklist[idx] < 999:  # цикл добавления элементов в массив до максимального нечётного числа
    checklist.append(checklist[idx] + 2)
    idx += 1
for idx3 in range(len(checklist)):  # цикл возведения в куб элементов массива
    checklist[idx3] **= 3
# до этого момента базовая часть задания
total_sum = 0  # сумма необходимых чисел в массиве
for num_checklist in checklist:
    x = 10  # переменная для деления на десятки
    units = num_checklist % x  # изначальное количество единиц
    sum_num_checklist = units  # изначальная сумма цифр в числе равна едининицам в конце
    while num_checklist // x >= 1:
        sum_num_checklist += num_checklist % (x * 10) // x
        x *= 10
    if not sum_num_checklist % 7:  # проверка кратности 7
        total_sum += num_checklist  # прибавляем к сумме элемент списка, прошедший условие кратности
print(total_sum)
