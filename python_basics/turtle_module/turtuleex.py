import turtle
import math
def square(t,n):
    for i in range(n):
        t.fd(150)#pixels length
        t.lt(90)#angle

def polygon(t,l,n):
    for i in range(n):
        t.fd(l)
        t.lt(360/n)
def Circle(t,r):
    circumference=2*math.pi*r
    n=int(circumference/3)+1
    l=circumference/n
    polygon(t,l,n)
    # for i in range(1,n,1):
    #     t.circle(r*i)#concurrent circles

    
    

bob=turtle.Turtle()
Circle(bob,20)
turtle.mainloop()