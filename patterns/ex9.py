n=int(input("enter"))
# for i in range(0,n):
#     print(' '*(n-(i+1)),'*'*(i+(i+1)),' '*(n-(i+1)),end='\n')
for i in range(0,n):
    for j in range(n,i+1,-1):
        print(' ',end='')
    for k in range(0,(i*2)+1,1):
        print('*',end='')
    print()
