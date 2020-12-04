import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('for_task_07.txt', 'r') as file:

    for data in file:
        name, firm, earning, damage = data.split()
        profit[name] = float(earning) - float(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1

    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')

    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')

    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('for_task_07_new', 'w') as writing_file:
    json.dump(profit, writing_file)
