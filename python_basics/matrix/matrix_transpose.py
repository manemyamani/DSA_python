from numpy import *
arr1=array([[1,2,3],
            [4,5,6],
            [7,8,9]
            ],int
           )
arr2=empty((3,3),int)
for i in range(0,3):
    for j in range(0,3):
        arr2[i][j]=arr1[j][i]

print(arr1)
print(arr2)