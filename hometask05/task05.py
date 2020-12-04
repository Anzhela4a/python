# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
user_file = open('For_task_05.txt', 'w')

user_input = list(input('Введите числа через пробел>>>'))
user_data = [int(x) for x in user_input if x != ' ']

total = 0
for ind in range(len(user_data)):
    total += user_data[ind]

user_file.write(str(total))
user_file.close()
