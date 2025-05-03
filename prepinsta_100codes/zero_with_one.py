n=input("enter number")
# new=n.replace('0','1')
# print(new)
new=" "
for i in n:
    if i=='0':
        new=new+'1'
     
    else:
        new=new+i
        
print("the no is ",new)


