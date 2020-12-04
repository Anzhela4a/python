with open('for_task_03.txt') as file:
    file_dict = {}
    for data in file:
        name, salary = data.split()
        file_dict[name] = float(salary)
        if float(salary) < 20000:
            print(f'{name} получает меньше 20 000,0 рублей')
    print(f'Средняя заработная плата>>> {sum(list(file_dict.values()))/len(list(file_dict.values()))}')

file.close()
