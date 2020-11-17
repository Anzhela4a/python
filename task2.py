user_str = list(input('Введите список: '))
print(user_str[1::2])
# if len(user_str) % 2 == 0:
#     user_str[::2], user_str[1::2] = user_str[1::2], user_str[::2]
# else:
#     el = user_str.pop()
#     user_str[::2], user_str[1::2] = user_str[1::2], user_str[::2]
#     user_str.append(el)
#
# print(*user_str)
