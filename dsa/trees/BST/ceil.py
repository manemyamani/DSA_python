class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def ceil_fn(root,key):
    ceil=float('Inf')
    while(root):
        if root.val==key:
            ceil=root.val
            return ceil
        if key>root.val:
            root=root.right
        else:
            if root.val<ceil:
                ceil=root.val
            root=root.left
            
    return ceil



root=Node(10)
root.left=Node(5)
root.right=Node(13)
root.right.left=Node(11)
root.right.right=Node(14)
root.left.left=Node(3)
root.left.right=Node(6)
root.left.right.right=Node(9)
root.left.left.left=Node(2)
root.left.left.right=Node(4)
k=ceil_fn(root,8)
print(k)