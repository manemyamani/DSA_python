def fun():
    print('+'.ljust(5,'-'),end='')
    print('+'.ljust(5,'-'),'+')
    for i in range(0,4):
        print('|'.ljust(5,' '),end='')
        print('|'.ljust(5,' '),'|')
    print('+'.ljust(5,'-'),end='')
    print('+'.ljust(5,'-'),'+')
    for i in range(0,4):
        print('|'.ljust(5,' '),end='')
        print('|'.ljust(5,' '),'|')
    print('+'.ljust(5,'-'),end='')
    print('+'.ljust(5,'-'),'+')
fun()


