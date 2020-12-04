user_file = open('for_task_01.txt', 'w')
user_data = []
try:
    while user_data != '':
        user_data = str(input('Введите данные для записи в файл>>>'))
        user_file.write(user_data + '\n')
finally:
    user_file.close()
