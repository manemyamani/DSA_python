num=input("enter binary")
sum=0
k=len(num)
for i in range(k):
    len=int(num[i:i+1])
    sum=sum+len*(2**(k-(i+1)))
    
print(sum)
