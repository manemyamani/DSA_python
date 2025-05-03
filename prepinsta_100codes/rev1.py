def reverse(self, x):
        sum=0
        flag=0
        if x<0:
            x=abs(x)
            flag=1
        while x!=0:
            rem=int(x%10)
            sum=sum*10+rem
            x=x//10
        if flag==1:
            return -sum
        return sum

p=reverse(1534236469)