from numpy import *
arr1=array([[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
            ],int
           )
arr2=empty((4,4),int)
k=-1
for i in range(3,-1,-1):
    k=k+1
    for j in range(0,4):
        arr2[k][j]=arr1[j][i]
print(arr2)