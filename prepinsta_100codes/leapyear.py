n=int(input("enter year"))
if (n%400==0 or (n%4==0 and n%100!=0)):
    print("leap year")
else:
    print("not a leap year")
   