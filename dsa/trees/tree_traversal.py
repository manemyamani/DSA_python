class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.data,end=" ")
    in_order(root.right)
def pre_order(root):
    if root is None:
        return
    print(root.data,end=" ")
    pre_order(root.left)
    pre_order(root.right)
def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data,end=" ")
root=Node(4)
root.left=Node(2)
root.right=Node(6)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.right=Node(8)
print("inorder traversal of a tree is :",end=" ")
in_order(root)


