class Node :
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
    def insert(self,value,index):
        new1=Node(value)
        if index==0:
            new1.next=self.head
            self.head=new1
            return
        temp=self.head
        for _ in range(index-1):
            temp=temp.next
        new1.next=temp.next
        temp.next=new1
    def remove(self,value):
        temp=self.head
        if temp and temp.value==value:
            self.head=temp.next
            return
        prev=None
        while(temp and temp.value!=value):
            prev=temp
            temp=temp.next
        prev.next=temp.next
    def get(self,index):
        if index==0:
            return self.head.value
        temp=self.head
        for _ in range(index):
            if not temp:
                raise IndexError('cant find the index and index out of range')
            temp=temp.next
        if temp:
            return temp.value
    def display(self):
        temp=self.head
        while(temp):
            print(temp.value,"-->",end=" ")
            temp=temp.next
        print(None)
l=Linkedlist()
l.append(1)
l.append(2)
l.append(4)
l.insert(3,1)
l.remove(2)
print(l.get(2))
l.display()
            
