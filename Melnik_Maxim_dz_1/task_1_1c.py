duration = input('Enter time duration in seconds ')
duration = int(duration)
hours = duration // 3600  # часы
minute = duration % 3600 // 60  # минуты
sec = duration % 3600 % 60  # секунды
print(str(hours) + ' h ' + str(minute) + ' m ' + str(sec) + ' s')
