class Solution:
    def combinationSum(self, candidates, target):
        result=[]
        def fn(i,arr,target,lst):
                if i==len(arr) or target<0:
                    if target==0:
                         result.append(lst[:])
                    return
                if arr[i]<=target:
                    lst.append(arr[i])
                    fn(i,arr,target-arr[i],lst)
                    lst.remove(arr[i])
                fn(i+1,arr,target,lst)
        fn(0,candidates,target,[])
        return result
s=Solution()
k=s.combinationSum([2,3,6,7],7)
print(k)

