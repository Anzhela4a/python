seconds = int(input('Введите количество секунд'))

hours_number = seconds // 3600
minutes_number = (seconds % 3600) // 60
seconds_number = seconds % 60

print('{}:{}:{}'.format(hours_number, minutes_number, seconds_number))
