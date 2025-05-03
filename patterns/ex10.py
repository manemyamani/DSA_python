n=5
for i in range(0,n):
    for j in range(0,n-(i+1)):
        print('*',end=' ')
    c=1
    for k in range(n-(i+1),n):
        print(c,end=" ")
        c=c+1
    print(' ')
for i in range(0,n):
    c=1
    for j in range(0,n-(i+1)):
        print(c,end=' ')
        c=c+1
    for k in range(n-(i+1),n):
        print("*",end=' ')
    print(' ')