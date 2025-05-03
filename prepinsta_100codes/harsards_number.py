temp=int(input("enter number"))
num=temp
sum=0
while num!=0:
    rem=int(num%10)
    sum=sum+rem
    num=num/10
if temp%sum==0:
    print(temp,"is harshards_number")