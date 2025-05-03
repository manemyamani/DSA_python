n=int(input("enter "))
for i in range(0,n):
    for j in range(n,i+1,-1):
        print(' ',end='')
    if i==0 or i==n:
        for k in range(0,(i*2)+1,1):
            print('*',end='')
    
        
    print()