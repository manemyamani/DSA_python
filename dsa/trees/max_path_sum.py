class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
global maxi
maxi=0
def find(root):
    global maxi
    if root==None:
        return 0
    lh=find(root.left)
    rh=find(root.right)
    maxi=max(maxi,lh+rh+root.data)
    return root.data+max(lh,rh)



root=Node(-10)
root.right=Node(20)
root.left=Node(9)
root.right.left=Node(15)
root.right.right=Node(7)
find(root)                  
print(maxi)