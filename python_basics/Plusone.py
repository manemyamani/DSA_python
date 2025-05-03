def plusOne(digits):
    k=len(digits)
    sum=0
    for i in range(1,k+1):
        sum=sum+i*(10**(k-i))
    sum=sum+1
    lst=[]
    while(sum):
        lst.append(sum%10)
        sum=sum//10
    lst.reverse()
    return lst
list=[4,3,2,1]
list1=plusOne(list)
print(list1)