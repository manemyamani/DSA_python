num1,den1=map(int,list(input("enter fraction").split('/')))
num2,den2=map(int,list(input("enter fraction").split('/')))
def gcd(a,b):
    k=b%a
    if k==0:
        return a
    else:
        return gcd(k,a)
def lcm(num1,num2):
    max=num1 if num1>num2 else num2
    min=num1 if num1<num2 else num2
    for i in range(1,max+1):
        if((max*i)%min==0):
            result=max*i
            break
    return result
if den1==den2:
    num=num1+num2
    res=gcd(num,den1)
    print("the addition=",num//res,'/',den1//res)
else:
    res=lcm(den1,den2)
    r1=res//den1
    r2=res//den2
    num=r1*num1+r2*num2
    res1=gcd(num,res)
    print("the addition=",num//res1,'/',res//res1)
