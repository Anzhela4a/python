my_list = [7, 5, 3, 3, 2]

while True:
    try:
        user_num = int( input( 'Введите число>>>' ) )
        my_list.append(user_num)
        my_list.sort(reverse=True)
        print(my_list)

    except ValueError:
        print('Неверное число')

    except KeyboardInterrupt:
        exit()
