user_a = int(input('Введите первое число>>>'))
user_b = int(input('Введите второе число>>>'))

def calculate(a, b):
    try:
        return print(a/b)
    except TypeError or ValueError:
        print('Не является числом')
        return
    except ZeroDivisionError:
        print('Деление на 0 невозможно')
        return

calculate(user_a, user_b)
