class A:
    def __init__(self):
        print("from class A")
class B:
    
    def __init__(self):
        #super().__init__()
        print("from class B")
class C(A,B):
    def __init__(self):
        super().__init__()
        B.__init__(self)
        print("from c")
a1=C()
