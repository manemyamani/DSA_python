class A:
    def execute(self):
        print("running in A")
class B:
    def execute(self):
        print("walking in B")
class C:
    def code(self,idle):
        idle.execute()

b=A()
a1=C()

a1.code(b)