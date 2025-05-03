class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def append(self,value):
        new1=Node(value)
        if not self.head:
            self.head=new1
            return
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=new1
    def rotate(self,k):
        cnt=0
        temp=self.head
        while(temp.next):           
            temp=temp.next
            cnt=cnt+1
        temp.next=self.head
        if k%cnt==0:
            return
        k=k%cnt
        s=cnt-k      
        current=self.head
        for _ in range(0,s):
            current=current.next
        self.head=current.next
        current.next=None
        
    def display(self):
        temp=self.head
        while(temp):
            print(temp.value,"-->",end=" ")
            temp=temp.next
        print(None)
l=Linkedlist()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.rotate(2)
l.display()
