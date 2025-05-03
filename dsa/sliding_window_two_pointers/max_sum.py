list=[-1,2,3,3,4,5,-1]
k=4
max=float('inf')
sum=sum(list[0:k])
max=sum
for i in range(0,len(list)-k):
    if sum>max:
        max=sum
    sum=sum-list[i]+list[i+k]
print(max)