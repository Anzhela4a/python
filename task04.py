# user_number = list(input('Введите целое положительное число >>> '))
# print(max(user_number))

user_number = input('Введите целое положительное число >>> ')
max_number = 9

while max_number >= 0:
    if str(max_number) in user_number:
        print(max_number)
        break
    else:
        max_number = max_number - 1
