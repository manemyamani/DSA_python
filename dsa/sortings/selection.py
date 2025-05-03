from array import *
def selectionsort(arr,n):
    for i in range(0,n):
        index=i
        for j in range(i+1,n):
            if(arr[index]>arr[j]):
                index=j               
        arr[i],arr[index]=arr[index],arr[i] 
arr=array('i',[])
n=int(input("enter the size"))
for i in range(0,n):
    arr.append(int(input("enter element")))
selectionsort(arr,len(arr))
print(arr)