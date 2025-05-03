class NewNode:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
    def insert_end(self,val):
        new=NewNode(val)
        if self.head==None:
            self.head=new
            return
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=new
        new.prev=temp
    def reverse(self):
        current=self.head
        while(current!=None):
            temp=current.prev
            current.prev=current.next
            current.next=temp
            current=current.prev
        self.head=temp.prev
    def display(self):
        temp=self.head
        while(temp):
            print(temp.val,end="-->")
            temp=temp.next
l=DLL()
l.insert_end(20)
l.insert_end(25)
l.insert_end(30)
l.insert_end(35)
l.reverse()
l.display()

        
    

