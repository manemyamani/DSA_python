from array import *
arr=array('i',[])
n=int(input("enter the size"))
for i in range(0,n):
    arr.append(int(input("enter element")))
k=int(input("enter the element to search"))
for i  in range(0,n):
    if arr[i]==k:
        print(k,"is found at index of",i+1)
        break
else:
    print("not found")


