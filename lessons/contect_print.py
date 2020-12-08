with open( 'data.txt', 'w' ) as printable:
    string = ['John', 'Kate']

    for x in string:
        print(x, file=printable)