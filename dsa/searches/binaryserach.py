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
arr=sorted(arr)
l=binarysearch(0,n-1,k)
if l>=0:
    print(k,'element is found at index',l+1)
else:
    print("not found")
