arr=[1,2,4,2,1,5]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)