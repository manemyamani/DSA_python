class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        self.m1=self.m1+other.m1
        self.m2=self.m2+other.m2
        m3=Student(self.m1,self.m2)
        return m3
    def __sub__(self,other):
        self.m1=self.m1-other.m1
        self.m2=self.m2-other.m2
        m3=Student(self.m1,self.m2)
        return m3
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)

    
s1=Student(1,2)
s2=Student(3,4)
s3=s1+s2
print(s3)