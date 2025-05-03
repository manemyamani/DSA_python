class A:
    def __init__(self):
        print("from class A")
class B:
    
    def __init__(self,x):
        #super().__init__()
        print(f"from class B",x)
class C(A,B):
    def __init__(self,x):
        super().__init__()
        B.__init__(self,x)
        print("from c")
a1=C(1)
