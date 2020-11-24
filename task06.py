from itertools import count, cycle
start_el_a = int(input('Введите стартовое значение >>'))
for el in count(start_el_a):
    if el <= 10:
        print(f'{el}')
    else:
        break

start_el_b = input('Введите стартовое значение >>')
ind = 0
for el in cycle(start_el_b):
    if ind >= 10:
        break
    print(el)
    ind += 1
