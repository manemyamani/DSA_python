s="Amma".lower()
i=0
n=len(s)
while(i<n//2):
    if(s[i]!=s[n-i-1]):
        print("not palindrome")
        break
    else:
        i=i+1
if(i==n//2):
    print("palidrome")
