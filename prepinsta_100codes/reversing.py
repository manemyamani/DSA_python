num=int(input("enter number"))
sum=0
while num!=0:
    rem=int(num%10)
    sum=sum*10+rem
    num=num//10
print(sum)
