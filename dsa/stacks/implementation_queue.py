from collections import deque
class queue:
    def __init__(self):
        self.q=deque()
    def push(self,val):
        s=len(self.q)
        self.q.append(val)
        for i in range(0,s):
            self.q.append(self.q.popleft())
            
    def pop(self):
        self.q.popleft()
    def top(self):
        print(self.q[0])
    def display(self):
        for i in self.q:
            print(i)
k=queue()
k.push(1)
k.push(2)
k.push(3)
k.display()
k.top()
k.pop()
