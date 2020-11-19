counter = 0
while True:
    user_a = int(input('Целое положительное число>>>'))
    user_b = int(input('Целое отрицательное чило>>>'))
    counter += 1
    if user_a > 0 | user_b < 0:
        break
    elif (user_a < 0 | user_b) or (user_b > 0 | user_a < 0) | counter > 0:
        print('Неверные значения! Попробуте снова.')
        continue

def my_func(a, b):
    try:
        return print(a**abs(b))
    except TypeError:
        print('Не является числом')
        return

my_func(user_a, user_b)