class Solution:
    def __init__(self):
        self.mem={}
    def fib(self, n: int) -> int:
        if n in self.mem:
            return self.mem[n]
        if n==0:
            return 0
        if n==1:
            return 1
        self.mem[n]=self.fib(n-1)+self.fib(n-2)
        return self.mem[n]
k=Solution()
print(k.fib(7))