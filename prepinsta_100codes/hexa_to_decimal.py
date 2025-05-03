# def fn(len):
#     if len=='A':
#         return 10
#     elif len=='B':
#         return 11
#     elif len=='C':
#         return 12
#     elif len=='D':
#         return 13
#     elif len=='E':
#         return 14
#     elif len=='F':
#         return 15
#     else:
#         return int(len)
    

# num=input("enter hexa")
# sum=0
# k=len(num)
# for i in range(k):
#     len=num[i:i+1]
#     m=fn(len)
#     sum=sum+m*(16**(k-(i+1)))  
# print(sum)

num=input("enter hexa")
sum=0
count=0
n=len(num)
for i in range(n-1,-1,-1):
    if '0'<=num[i]<='9':
        k=int(num[i])
        sum=sum+k*(16**count)
        count=count+1
    elif 'A'<=num[i]<='F':
        k=ord(num[i])-55
        sum=sum+k*(16**count)
        count=count+1
print(sum)



