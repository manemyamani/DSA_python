# num=int(input("enter number"))
arm=[]
for num in range(1,1000):
    sum=0
    temp=num
    while(temp>0):
        k=int(temp%10)
        sum=sum+k**3
        temp=temp/10
    if sum==num:
         arm.append(num)
print("the armstrong numbers are",arm)
# num="370"
# k=len(num)
# sum=0
# for i in num:
#     sum+=int(i)**k
# if sum==int(num):
#     print(num,"is armstrong number")
