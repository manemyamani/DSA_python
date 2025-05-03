class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,val):
        new=Node(val)
        if self.root==None:
            self.root=new
            return
        temp=self.root
        while True:
            if val<temp.val:
                if temp.left is None:
                    temp.left=new
                    return
                temp=temp.left
                
            if val>temp.val:
                if temp.right is None:
                    temp.right=new
                    return
                temp=temp.right
    # def insert(self,root,val): #recursive
        
    #     if root==None:
    #         return Node(val)
    #     elif val<root.val:
    #         root.left=self.insert(root.left,val)
    #     elif val>root.val:
    #         root.right=self.insert(root.right,val)
    #     return root

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.val,end=" ")
            self.inorder(node.right)
    def preorder(self,node):
        if node:
            print(node.val,end=" ")
            self.preorder(node.left)           
            self.preorder(node.right)

    def search(self,root,val):
        if root is None:
            return None
        elif root.val==val:
             return "found"                
        elif root.val<val:
            return self.search(root.right,val)
        elif root.val>val:
            return self.search(root.left,val)

    # def delete(self,val):
    #     prev=None
    #     current=self.root
    #     while(current and current.val!=val):
    #         if val>current.val:
    #             prev=current
    #             current=current.right
    #         elif val<current.val:
    #             prev=current
    #             current=current.left
        
            



b=BST()
list=[13,7,15,3,8,14,19,18]
for i in list:
    b.insert(i)
print("inorder traversal : ")
b.inorder(b.root)
print()
print(b.search(b.root,8))

        
