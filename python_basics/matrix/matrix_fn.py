from numpy import *
arr=matrix('1,2,3;4,5,6;7,8,9') #also possible for matrix
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
m=matrix(arr1)

m1=matrix(arr2)
#print(diagonal(m))
#print(m.max())
m3=m+m1
print(m3)
m4=m*m1
print(m4)
# print(arr)