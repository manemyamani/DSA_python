from numpy import *
arr1=array([[1,2,3],
            [4,5,6],
            [1,4,3]
            ]
           )
arr2=array([[1,4,3],
            [7,5,6],
            [1,4,2]
            ]
           )
arr3=empty((3,3))
for i in range(0,3):
    for j in range(0,3):
        arr3[i][j]=arr1[i][j]+arr2[i][j]
print(arr3)