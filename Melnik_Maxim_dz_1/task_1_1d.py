duration = input('Enter time duration in seconds ')
duration = int(duration)
days = duration // 86400  # дни
hours = duration % 86400 // 3600  # часы
minute = duration % 86400 % 3600 // 60  # минуты
sec = duration % 86400 % 3600 % 60  # секунды
print(str(days) + ' d ' + str(hours) + ' h ' + str(minute) + ' m ' + str(sec) + ' s')
