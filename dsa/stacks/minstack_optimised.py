class minstack:
    def __init__(self):
        self.stack=[]
        self.min=None
    def push(self,val):
        if not self.stack:
            self.stack.append(val)
            self.min=val
        elif val<self.min:
            original=2*val-self.min
            self.stack.append(original) 
            self.min=val           
        else:
            self.stack.append((val))
    def min1(self):
        if self.stack is not None:
            print("the minimum element is",self.min)
        else:
            print("stack is empty")
    def pop(self):
        if not self.stack:
            print("Stack is empty.")
            return
        original=self.stack[-1]
        if original<self.min:
            
            self.min=2*self.min-original
        self.stack.pop()
    def peek(self):
        if not self.stack:
            print("Stack is empty.")
            return None
        if self.stack[-1]<self.min:
            return self.min
        return self.stack[-1]
    def display(self):
        print("Stack from top to bottom:")
        temp_stack = []
        current_min = self.min
        for i in self.stack:
            if i < current_min:
                temp_stack.append(current_min)
                current_min = 2 * current_min - i
            else:
                temp_stack.append(i)

        for val in reversed(temp_stack):
            print(val, end=" ")
        print()
m=minstack()
m.push(2)
m.push(4)
m.push(1)
m.push(5)
m.display()
m.min1()
m.pop()
m.pop()
m.min1()