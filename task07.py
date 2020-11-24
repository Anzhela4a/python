def get_factorial(n):
    result = 1
    for x in range(1, n + 1):
        result *= x
        yield result

n = int(input('Введите значение>>>'))

for el in get_factorial(n):
    print(el)