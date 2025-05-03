num=int(input("enter"))
sum=0
for i in range(1,num//2+1):
    if num%i==0:
        sum=sum+i
if sum==num:
    print(num,"is perfect number")
else:
    print(num,"not a perfect number")