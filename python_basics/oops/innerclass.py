class Student:
    def __init__(self,name,roll):
        self.name=name 
        self.roll=roll
    def show(self):
        print(self.name,self.roll)
    class Laptop:
        def __init__(self,brand,os):
            self.brand=brand
            self.os=os
        def show(self):
            print(self.brand,self.os)
s1=Student('yamini',28)
s1.show()
lap1=Student.Laptop('hp','intel')
lap1.show()
    