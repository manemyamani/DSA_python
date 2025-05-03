def fn(i,lst,sum):
    if i>=n:
        if sum==2:
            print(lst)
        return
    lst.append(arr[i])
    fn(i+1,lst,sum+arr[i])
    lst.remove(arr[i])
    fn(i+1,lst,sum)
arr=[1,2,1]
n=len(arr)
lst=[]
fn(0,lst,0)