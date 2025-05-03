def fn(i,arr,target,lst):
    if i==n:
        if target==0:
            print(lst)
        return
    if arr[i]<=target:
        lst.append(arr[i])
        fn(i,arr,target-arr[i],lst)
        lst.remove(arr[i])
    fn(i+1,arr,target,lst)
arr=[2,3,4,7]
n=len(arr)
lst=[]
fn(0,arr,7,lst)