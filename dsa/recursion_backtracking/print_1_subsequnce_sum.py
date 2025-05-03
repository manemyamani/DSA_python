def fn(i,lst,sum):
    if i>=n:
        if sum==2:
            print(lst)
            return True
        else:
            return False
    lst.append(arr[i])
    if(fn(i+1,lst,sum+arr[i])==True):
        return True
    lst.remove(arr[i])
    if(fn(i+1,lst,sum)==True):
        return True
arr=[1,2,1]
n=len(arr)
lst=[]
fn(0,lst,0)