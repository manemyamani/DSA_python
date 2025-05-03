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
        return self.head
    def add(Self,head1,head2):
        t1=head1
        t2=head2
        dummy=Node(-1)
        carry=0
        current=dummy
        while(t1!=None or t2!=None):
            sum=carry
            if t1!=None:
                sum=sum+t1.value
                t1=t1.next
            if t2!=None:
                sum=sum+t2.value
                t2=t2.next
            new=Node(sum%10)
            carry=sum/10
            current.next=new
            current=current.next
            if carry:
                new=Node(carry)
                current.next=new
            return dummy.next
            
        
    def display(self):
        temp=self.head
        while(temp):
            print(temp.value,"-->",end=" ")
            temp=temp.next
        print(None)




l1=Linkedlist()
l1.append(1)
x=l1.append(2)
l2=Linkedlist()
l2.append(2)
y=l2.append(3)
l3=Linkedlist()
l3.add(x,y)
l3.display()