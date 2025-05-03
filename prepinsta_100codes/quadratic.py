import math
a,b,c=map(int,input("enter a,b,c").split(' '))
d=b*b-4*a*c
if d<0:
    print("no real roots")
elif d==0:
    x=-b/(2*a)
    print("their exists equal real roots, the roots are : ",x,x)
elif d>0:
    x=(-b+math.sqrt(d))/2*a
    y=(-b-math.sqrt(d))/2*a
    print("their exists 2 real roots, the roots are : ",x,y)

