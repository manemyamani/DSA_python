from numpy import *
nums1=array([1,2,3,4,5])
nums2=nums1.copy() #deep copy
nums1[2]=13
print(nums1)
print(nums2)