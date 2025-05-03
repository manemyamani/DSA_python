# n=int(input("enter the number"))
# num1=0
# num2=1
# print(num1,num2,end=" ")
# for i in range(2,n):
#     num3=num1+num2
#     num1=num2
#     num2=num3
#     print(num3,end=" ")
def fib(num):
    if num==0:
        return 0
    if num==1:
        return 1
    return fib(num-1)+fib(num-2)

# for i in range(0,5):
#     print(fib(i),end=" ")
# for nth term
print(fib(7))