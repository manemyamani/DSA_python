def post_infix(s):
    stack=[]
    for i in s:
        if i.isalnum():
            stack.append(i)
        elif i in '+-*/':
            b=stack.pop()
            a=stack.pop()
            res='('+a+i+b+')'
            stack.append(res)
    return stack[-1]
        
s="ab-de+f*/"
k=post_infix(s)
print(k)
