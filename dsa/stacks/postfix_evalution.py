def evalution(s):
    stack=[]
    for i in s:
        if i.lstrip('-').isdigit():
            stack.append(i)
        elif i in '+-*/':
            b=stack.pop()
            a=stack.pop()
            res=eval(f"{a}{i}{b}")
            stack.append(res)
    return stack[-1]
        
s="732+52-*+"
k=evalution(s)
print(k)
