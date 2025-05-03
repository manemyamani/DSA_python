x,y=map(int,list(input("enter the quadrants x y").split(' ')))
if x>0 and y>0:
    print(r'{x,y} = are in first quadrant')
elif x < 0 and y > 0:
    print("point (", x, ",", y, ") lies in the Second quadrant")
elif x < 0 and y < 0: 
    print("point (", x, ",", y, ") lies in the Third quadrant")
elif x > 0 and y < 0:
    print("point (", x, ",", y, ") lies in the Fourth quadrant")
