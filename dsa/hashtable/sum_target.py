arr=[1,2,3,4]
target=6
hash_table={}
for i in range(len(arr)):
    compliment=target-arr[i]
    if compliment in hash_table:
         print(hash_table[compliment],i)
    hash_table[arr[i]]=i