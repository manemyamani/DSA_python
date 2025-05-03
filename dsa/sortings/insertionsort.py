from array import *
def insertion(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr





arr=array('i',[56,12,54,36,28])
arr=insertion(arr)
print(arr)