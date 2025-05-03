class Student:
    college='JNTU-GV'
    def __init__(self,name,roll):
        self.name=name #instance variables
        self.roll=roll
    def show(self): #instance method
        print(self.name,self.roll,end=' ')
    @classmethod 
    def clg(cls): #class method
        print(cls.college)

    @staticmethod
    def info():
        print("this info about students")
s1=Student('yamini',28)
s1.show()
Student.clg()
Student.info()