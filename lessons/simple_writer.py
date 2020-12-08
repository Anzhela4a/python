my_file = open( 'data.txt', 'w' )

if my_file.writable():
    my_file.write('Update\n')

    string = ['John\n', 'Kate\n']
    my_file.writelines(string)
else:
    print('can not write')

my_file.close()