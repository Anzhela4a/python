portal_name = str('Литературный онлайн-клуб')
common_users = int(25)

print('Добро пожаловать в наш {}! Количество пользователей уже составляет {} человек'.format(portal_name, common_users))

user_name = str(input('Укажите ваш логин: '))

print('Привет, {}! Ты стал {}-м пользователем! Поздравляем!'.format(user_name, common_users+1,))
