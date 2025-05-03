def post_infix(s):
    stack=[]  
    for i in range(len(s)-1,-1,-1):
        if s[i].isalnum():
            stack.append(s[i])
        elif s[i] in '+-*/':
            a=stack.pop()
            b=stack.pop()
            res=a+b+s[i]
            stack.append(res)
    return stack[-1]
        
s="/-ab*+def"
k=post_infix(s)
print(k)