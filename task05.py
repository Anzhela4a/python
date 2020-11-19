answer = 0
while True:
    user_list = input('Введите числа через пробел>>>')
    if user_list[-4:] == 'exit':
        answer += sum(map(int,user_list[:-4].split()))
        print(answer)
        break
    else:
        answer += sum(map(int,user_list.split()))
        print(answer)
