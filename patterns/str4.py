p=1
n=5
for i in range(0,n):
    print((n-p)*' ',(i+p)*'*',(n-p)*' ')
    p=p+1
p=4
for i in range(n,0,-1):
    print((n-p-1)*' ',(i+p)*'*',(n-p-1)*' ')
    p=p-1

