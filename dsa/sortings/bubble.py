from array import *
arr=array('i',[])
n=int(input("enter the size"))
for i in range(0,n):
    arr.append(int(input("enter element")))
for i in range(0,n-1):
    swap=False
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swap=True
    if not swap:
        break
print(arr)