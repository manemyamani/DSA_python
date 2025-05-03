def fn(i,lst,sum):
    if i>=n:
        if sum==2:
            return 1
        return 0
    lst.append(arr[i])
    l=fn(i+1,lst,sum+arr[i])
    lst.remove(arr[i])
    r=fn(i+1,lst,sum)
    return l+r
arr=[1,2,1]
n=len(arr)
lst=[]
print(fn(0,lst,0))