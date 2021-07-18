duration = input('Enter time duration in seconds ')
duration = int(duration)
minute = duration // 60  # минуты
sec = duration % 60  # секунды
print('0 h ' + str(minute) + ' m ' + str(sec) + ' s')
