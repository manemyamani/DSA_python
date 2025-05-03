def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter the no of students"))
r=int(input("enter the seats"))
permutation=fact(n)//fact(n-r)
print('total arrangements are=',permutation)