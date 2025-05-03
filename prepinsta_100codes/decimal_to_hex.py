num=int(input("enter"))
li=[]
while(num>0):
    k=num%16
    if k==10:
        li.append('A')
    elif k==11:
        li.append('B')
    elif k==12:
        li.append('C')
    elif k==13:
        li.append('D')
    elif k==14:
        li.append('E')
    elif k==15:
        li.append('F')
    else:
        li.append(k)
    num=num//16
li.reverse()
print(li)
