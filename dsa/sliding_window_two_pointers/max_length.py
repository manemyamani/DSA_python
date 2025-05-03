arr=[2,5,1,7,10]
l=0
r=0
k=14
n=len(arr)
maxlength=0
sum=0
while(r<n):
    sum=sum+arr[r]
    while(sum>k):
        sum=sum-arr[l]
        l=l+1
    if(sum<=k):
        maxlength=max(maxlength,r-l+1)
    r=r+1
print(maxlength)

