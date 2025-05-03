num=int(input("enter"))
li=[]
while(num>0):
    k=num%2
    li.append(k)
    num=num//2
li.reverse()
print(li)
