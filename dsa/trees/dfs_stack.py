class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def dfs(root):
    stack=[]
    if not root:
        return
    
    stack.append(root)
    while stack:
        temp=stack.pop()
        print(temp.value,end=' ')
        if temp.right:
            stack.append(temp.right)
        if temp.left:
            stack.append(temp.left)


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
dfs(root)
