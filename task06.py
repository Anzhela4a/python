def int_func(var):
    cap = var.title()
    return cap

var = input('Введите слово>>> ')
if var.find(' ') != -1:
    z = var.find(' ')
    var = var[:z]
print(int_func(var))
var = input('Введите предложение ')
print(int_func(var))
