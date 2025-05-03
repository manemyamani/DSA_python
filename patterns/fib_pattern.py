n1=0
n2=1
n3=0
for i in range(0,6):
    for j in range(0,i):
        n3=n1+n2
        print(n1,end=' ')
        n1=n2
        n2=n3
    print(' ')
