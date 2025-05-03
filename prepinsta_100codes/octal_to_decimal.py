num=int(input("enter binary"))
sum=0
count=0
while(num>0):
    k=num%10
    sum=sum+k*(8**count)
    num=num//10
    count=count+1

print(sum)
