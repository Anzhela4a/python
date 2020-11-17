month = int(input('Введите номер месяца: '))

month_dict = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}

for key, val in month_dict.items():
    if month in val:
        print(f'Это - {key}')
        break