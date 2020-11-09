profit = float(input('Введите значение выручки в рублях'))
costs = float(input('Введите значение издержек в рублях'))

if profit > costs:
    rent = (profit - costs) / profit * 100
    print('Компания работает в прибыль. Рентабельность составила ', '{:.1f}'.format(rent), '%')
    personal = int(input('Введите количество сотрудников'))
    personal_profit = (profit - costs) / personal
    print('Прибыль на одного сотрудника составляет ', '{:.2f}'.format(personal_profit), 'рублей')
elif profit < costs:
    print('Компания работает в убыток.')
else:
    print('Компания работает в ноль.')
