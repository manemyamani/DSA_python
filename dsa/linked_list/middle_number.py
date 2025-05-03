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
    def length(self):
        temp=self.head
        cnt=0
        while(temp!=None):
            cnt=cnt+1
            temp=temp.next
        return cnt
    def mid(self):
        k=self.length()
        mid=k//2+1
        return mid
l=Linkedlist()
l.append(1)
l.append(2)
l.append(6)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l.length()
print(l.mid())

