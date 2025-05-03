from collections import deque
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def zigzag(root):
    if not root:
        return
    queue=deque()
    queue.append(root)
    i=0
    while len(queue)!=0:
        if i%2==0:
            temp=queue.popleft()
            print(temp.value,end=' ')
            if temp.right:
                queue.append(temp.right)
                # print(temp.right.value,end=' ')
            if temp.left:
                queue.append(temp.left)
                # print(temp.left.value)
            i=i+1
        else:
            temp=queue[-1]
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            i=i+1

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
zigzag(root)
