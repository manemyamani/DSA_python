num1=int(input("enter numbers"))
num2=int(input())
max=num1 if num1>num2 else num2
min=num1 if num1<num2 else num2
for i in range(1,max+1):
    if((max*i)%min==0):
        result=max*i
        break
print(result)
