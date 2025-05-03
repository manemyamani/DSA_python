class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def push(self,val):
        new=Node(val)
        new.next=self.top
        self.top=new
    def pop(self):
        if not self.top:
            print("stack underflow")
        self.top=self.top.next       
    def peek(self):
        if not self.top:
            print("stack is empty")
        print(self.top.val)
    def size(self):
        temp=self.top
        cnt=0
        while(temp):
            temp=temp.next
            cnt=cnt+1
        print(cnt)
    def display(self):
        temp=self.top
        while(temp):
            print(temp.val,"-->",end=" ")
            temp=temp.next
        print(None)

s=stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.display()
s.pop()
s.display()
s.size()
s.peek()


