num=int(input("enter number"))
sum=0
while num!=0:
    rem=int(num%10)
    sum=sum+rem
    num=num/10
print(sum)
