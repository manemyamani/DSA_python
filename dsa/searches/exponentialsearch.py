from math import *
from array import *
def binarysearch(lb,up,k):
    if lb>up:
        return -1   
    mid=(lb+up)//2
    if arr[mid]==k:       
        return mid
    elif arr[mid]>k:
        up=mid-1
        return binarysearch(lb,up,k)
    elif arr[mid]<k:
        lb=mid+1
        return binarysearch(lb,up,k)
arr=array('i',[])
n=int(input("enter the size"))
for i in range(0,n):
    arr.append(int(input("enter element")))
k=int(input("enter the element to search"))
prev=0
step=1
while step<n and arr[min(step,n-1)]<k:      
        prev=step
        step=step*2    
pos=binarysearch(prev,min(step,n-1),k)
if pos!=-1:
     print("found at ",k)
else:
     print("not found")