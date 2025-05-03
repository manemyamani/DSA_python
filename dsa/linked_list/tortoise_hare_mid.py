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
    def mid(self):
        slow=fast=self.head
        while(fast.next!=None and fast!=None):
            slow=slow.next
            fast=fast.next.next
        print(slow.value)

l=Linkedlist()
l.append(1)
l.append(2)
l.append(6)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l.mid()