# str="1221"
# str2=str[::-1]
# if str==str2:
#     print(str,"is palindrome")

def isPalindrome(self, x):
        # remove if number is negative
        if x<0:
            return False
        temp=x
        sum=0
        while x>0:
             sum=sum*10+x%10
             x//=10
        if temp==sum:
            return True
        else:
            return False
        