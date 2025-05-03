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
    def reverse(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev 

    def palindrome(self):
        slow=fast=self.head
        while(fast and fast.next.next!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        second_half=self.reverse(slow.next)
        temp1=self.head
        temp2=second_half
        while(second_half):
            if(temp1.value!=second_half.value):
                return False
            temp1=temp1.next
            second_half=second_half.next
        self.reverse(temp2)
        return True




    

l=Linkedlist()
l.append(1)
l.append(2)
l.append(2)
l.append(1)
print(l.palindrome())
