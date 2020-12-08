import os

# if os.path.exists('data.txt'):
#     os.remove('data.txt')

current_dir = ''
files = os.listdir()

for x in files:
    # print(os.path.dirname(x))
    # print(os.path.dirname(f'./{x}'))
    # print(os.path.dirname(f'/ets/hosts'))
    # print( os.path.isdir( x ) )
    # print(os.path.isdir(f'./{x}'))
    print(os.path.split(x))

print(os.path.split('/ets/hosts'))
print(files)

print(os.path.join('/ets/hosts', 'file', 'hop', '1.txt'))