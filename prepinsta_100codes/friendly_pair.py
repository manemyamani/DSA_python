import math
def sum_factors(num):
    sum=0
    for i in range(1,num//2+1):
        if num%i==0:
            sum=sum+i
    print(sum)
    return sum
m=int(input("enter m "))
n=int(input("enter n "))
if (m//sum_factors(m))==(n//sum_factors(n)):
    print(m,n,"these are friendly_pair")