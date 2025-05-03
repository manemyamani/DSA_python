arr=[6,2,3,4,7,2,1,7,1]
l=0
k=4
r=len(arr)-1
sum=sum(arr[0:k])
cost=sum
for i in range(k-1,-1,-1):
    if sum>cost:
        cost=sum
    sum=sum-arr[i]
    sum=sum+arr[r]
    r=r-1
print(cost)
