class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:           
            return self.stack.pop()                    
    def is_empty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
    def peek(self):
        if self.is_empty():
            print("stack is empty")
        else:
            return self.stack[-1]
def run_program():
    s=Stack()
    while True:
        print("\nChoose an operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if Empty")
        print("5. Exit")
        k=int(input("enter any choice between [1-5]"))
        if k==1:
            s.push(int(input("enter element to push")))
        elif k==2:
            s.pop()
        elif k==3:
            s.peek()
        elif k==4:
            s.is_empty()
        elif k==5:
            print("terminating")
            break
#run_program()

        

