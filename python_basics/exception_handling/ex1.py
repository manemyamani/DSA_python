a=10
b=1
try:
    print(a/b)
    z=int(input("enter "))
except ZeroDivisionError as e:
    print("you should not divide by zero",e)
except ValueError as e:
    print("incorrect values are passed",e)
except Exception as e:
    print(e)
finally :
    print("executed")

