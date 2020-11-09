current_result = float(input('Введите количество киллометров, достигнутых в первый день пробежки'))
wish_result = float(input('Введите количество киллометров, которое желаете достигнуть'))
day = 1
if current_result < 0 or wish_result < 0:
    print('Введено неверное число')
else:
    while current_result < wish_result:
        print('{}-й день: {} км'.format(day, '%.2F' % (current_result)))
        current_result = current_result * 1.1
        day += 1
print('{}-й день: {} км'.format(day, '%.2F' % (current_result)))
print('ОТВЕТ: на {}-й день спортсмен достиг результата — не менее {} км'.format(day, wish_result))
