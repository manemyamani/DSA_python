class NewNode:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
    def insert_begining(self,val):
        new=NewNode(val)
        if self.head==None:
            self.head=new
            return 
        else:
            self.head.prev=new
            new.next=self.head
            self.head=new
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
    def insert_after(self,start,target):
        temp=self.head
        new=NewNode(target)
        while(temp.val!=start):
            temp=temp.next
        new.next=temp.next
        temp.next=new
        new.prev=temp
    def delete_beg(self):
        if self.head==None:
            return None
        print(self.head.val," is deleted")
        self.head=self.head.next
        self.head.prev=None
    def delete_end(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        print(temp.val," is deleted")
        temp.prev.next=None
    def delete_Value(self,val):
        temp=self.head
        while(temp.val!=val):
            temp=temp.next
        print(temp.val,"is deleted")
        temp.prev.next=temp.next
        temp.prev=temp.prev

    def display(self):
        temp=self.head
        while(temp):
            print(temp.val)
            temp=temp.next
l=DLL()
l.insert_begining(10)
l.insert_begining(5)
l.insert_end(20)
l.insert_end(25)
l.insert_after(10,15)
l.insert_end(30)
l.insert_end(35)
l.delete_beg()
l.delete_end()
l.delete_Value(25)
l.display()

        

