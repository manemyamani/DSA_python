from array import *
arr=array('i',[1,2,3,4,5])
l=0
r=len(arr)-1
while(l!=r):
    arr[l],arr[r]=arr[r],arr[l]
    l=l+1
    r=r-1
print(arr)