from sys import argv

script_name, hours, cost, bonus = argv

# print("Имя скрипта: ", script_name)
print("выработка в часах: ", hours)
print("ставка в час: ", cost)
print("премия: ", bonus)

def calculate_salary (hours, cost, bonus):
    try:
        return print(f'Заработная плата составляет: {int(hours) * int(cost) + int(bonus)}')
    except TypeError:
        print('Введены неверные значения')
        exit()

# print(calculate_salary(40, 2000, 1000))
calculate_salary (hours, cost, bonus)

