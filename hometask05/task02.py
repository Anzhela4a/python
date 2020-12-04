counter = open('for_task_02.txt')
data = counter.readlines()
ind = 0
print(f'Количество строк в файле {len(data)} строк')
try:
    while True:
        line = list(data[ind])
        print(f'{ind+1} строке {line.count(" ")+1} слов')
        ind +=1
except IndexError:
    exit()
