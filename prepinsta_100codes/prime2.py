from math import *
num=int(input("enter num"))
lst=[]
for i in range(2,num+1):
    for j in range(2,isqrt(i)+1):
        if i%j==0:
            break
    else:
        lst.append(i)
found_pairs=set()
for i in lst:
    b=num-i
    if b in lst and (b, i) not in found_pairs and (i, b) not in found_pairs:
        found_pairs.add((b,i))
print(found_pairs)


