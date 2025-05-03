def bin(i,j):
    global carry
    carry=0
    if i==1 and j==1:
        carry=1
        return 0
    elif i==1 and j==0:
        carry=0
        return 1
    elif i==0 and j==1:
        carry=0
        return 1
    elif i==0 and j==0:
        carry=0
        return 0
str1="11"
str2="1"


        