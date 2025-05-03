from numpy import *
arr1=array([[1,2,3],
            [4,5,6],
            [1,4,3]
            ],int
           )
arr2=array([[1,4,3],
            [7,5,6],
            [1,4,2]
            ],int
           )
arr3=zeros((3,3),int)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            arr3[i][j]+=arr1[i][k]*arr2[k][j]
print(arr3)