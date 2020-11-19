user_x = int(input('Введите первое число>>>'))
user_y = int(input('Введите второе число>>>'))
user_z = int(input('Введите третье число>>>'))

def my_func(*args):
    try:
        my_list = sorted(args)
        result = sum(my_list[1::])
        return print(result)
    except TypeError:
        print('Не является числом')
        return

my_func(user_x, user_y, user_z)
