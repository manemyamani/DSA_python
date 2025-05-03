nums=[1,2,3,1,2,3]
k=2
freq={}
for i in range(len(nums)):
    if nums[i] in freq:
        if i-freq[nums[i]]<=k:
            print(i,freq[nums[i]])
            print(True)
        else:
            print(False)
    freq[nums[i]]=i