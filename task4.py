user_str = input('Введите предложение')
my_srt = user_str.split()

for key, val in enumerate(my_srt,1):
    print(key, val[:10])
