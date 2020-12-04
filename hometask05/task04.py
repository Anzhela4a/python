russian_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []

with open('for_task_04.txt') as reading_file:
    for data in reading_file:
        data = data.split(' ', 1)
        new_file.append(russian_dict[data[0]] + '  ' + data[1])

with open('for_task_04_new.txt', 'w') as writing_file:
    writing_file.writelines(new_file)
