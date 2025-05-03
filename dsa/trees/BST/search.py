class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,root,val): #recursive    
        if root==None:
            return Node(val)
        elif val<root.val:
            root.left=self.insert(root.left,val)
        elif val>root.val:
            root.right=self.insert(root.right,val)
        return root
    def search(self,root,val):
        if root is None:
            return None
        elif root.val==val:
             return "found"
        elif root.val<val:
            return self.search(root.right,val)
        elif root.val>val:
            return self.search(root.left,val)
    def preorder(self,node):
        if node is None:
            return []
        return [node.val]+self.preorder(node.left)+self.preorder(node.right)
lst=[4,2,7,1,3]
b=BST()
for i in lst:
    b.root=b.insert(b.root,i)
l=b.search(b.root,2) 
print(l)   
