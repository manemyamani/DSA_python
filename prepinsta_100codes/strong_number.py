temp=int(input(" enter "))
def fact(num):
    res=1
    for i in range(1,num+1):
        res=res*i
    return res
sum=0
num=temp
while num!=0:
    rem=int(num%10)
    sum=fact(rem)+sum
    num=num//10
if temp==sum:
    print(temp,"is strong number")
else:
    print(temp,"is not an strong number")
