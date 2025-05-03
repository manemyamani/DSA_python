from array import *
def fn(arr,l,r):
    if l>=r:
        return
    arr[l],arr[r]=arr[r],arr[l]
    fn(arr,l+1,r-1)

arr=array('i',[1,2,3,4,5])
l=0
r=len(arr)-1
fn(arr,l,r)
print(arr)