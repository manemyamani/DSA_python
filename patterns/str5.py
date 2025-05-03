p=2
n=3
for i in range(n,0,-1):
    print((n-p)*' ',(i+p)*'*',(n-p)*' ')
    p=p-1
