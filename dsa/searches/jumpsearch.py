from math import *
from array import *
arr=array('i',[])
n=int(input("enter the size"))
for i in range(0,n):
    arr.append(int(input("enter element")))
k=int(input("enter the element to search"))
prev=0
step=0
flag=1
while step<n and arr[min(step,n-1)]<k:      
        prev=step
        step=step+isqrt(n)    
for i in range(prev,min(step,n-1)+1):
    if(arr[i]==k):
        print("found at ",i+1)
        break
else:
    print("not found")