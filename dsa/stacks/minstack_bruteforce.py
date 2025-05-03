class minstack:
    def __init__(self):
        self.stack=[]
        self.min=float('inf')
    def push(self,val):
        if val<self.min:
            self.min=val
            self.stack.append((val,self.min))
            
        else:
            self.stack.append((val,self.min))
    def min1(self):
        print("the minimum element is",self.stack[-1][1])
    def pop(self):
        self.stack.pop()
    def display(self):
        for i in self.stack:
            print(i,end=" ")

m=minstack()
m.push(2)
m.push(4)
m.push(1)
m.push(5)
m.min1()
m.pop()
m.pop()
m.min1()