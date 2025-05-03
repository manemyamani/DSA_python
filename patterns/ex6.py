n=int(input("enter "))
for i in range(0,n):
    for j in range(0,i+1):
        print(' ',end='')
    for k in range(0,n):
        print('*',end="")
    print()
