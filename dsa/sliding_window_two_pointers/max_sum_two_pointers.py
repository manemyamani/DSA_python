list=[-1,2,3,3,4,5,-1]
k=4
max=float('inf')
sum=sum(list[0:k])
max=sum
l=0
r=k
while(r<len(list)):
    if sum>max:
        max=sum
    sum=sum-list[l]+list[r]
    l=l+1
    r=r+1
print(max)