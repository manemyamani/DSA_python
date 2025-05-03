import turtle
def polygon(t,l,n):
    for i in range(n):
        t.fd(l)
        t.lt(360/n)
    t.home()
bob=turtle.Turtle()
polygon(bob,150,5)
turtle.mainloop()