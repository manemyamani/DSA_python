s="Amma".lower()
l=0
r=len(s)-1
while(l<=r):
    if s[l]==s[r]:
        l=l+1
        r=r-1
    else:
        print("not a palindrome")
        break
if(l>r):
    print("they are palindrome")