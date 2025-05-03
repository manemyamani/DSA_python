def fn(i,lst):
    if i>=n:
        print(lst)
        return
    lst.append(arr[i])
    fn(i+1,lst)
    lst.remove(arr[i])
    fn(i+1,lst)
arr=[3,2,1]
n=len(arr)
lst=[]
fn(0,lst)