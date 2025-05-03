def post_prefix(s):
    stack=[]
    for i in s:
        if i.isalnum():
            stack.append(i)
        elif i in '+-*/':
            b=stack.pop()
            a=stack.pop()
            res=i+a+b
            stack.append(res)
    return stack[-1]
        
s="ab-de+f*/"
k=post_prefix(s)
print(k)
