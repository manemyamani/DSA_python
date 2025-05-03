class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cnt=0       
        def fn(i,s1):
            nonlocal cnt
            if i==len(s):
                 if s1==t:
                     cnt=cnt+1
                 return
            s1=s1+s[i]
            fn(i+1,s1)
            s1=s1[:-1]
            fn(i+1,s1)
        fn(0,'')
        print(cnt)
            
s=Solution()
s.numDistinct('rabbbit','rabbit')
