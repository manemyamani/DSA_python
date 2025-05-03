def priority(s):
    if s=='^':
        return 3
    elif s=='*' or s=='/':
        return 2
    elif s=='+' or s=='-':
        return 1
    else:
        return -1
def infix_to_post(s):
    st=[]
    ans=""
    for i in s:
        if i.isalnum():
            ans=ans+i
        elif i=='(':
            st.append(i)
        elif i==')':
            while(not len(st)==0 and st[-1]!='('):
                ans=ans+st[-1]
                st.pop()
            st.pop()
        else:
            while(not len(st)==0 and priority(i)<=priority(st[-1])):
               ans=ans+st[-1]
               st.pop()
            st.append(i)
    while(not len(st)==0):
        ans=ans+st[-1]
        st.pop()
    return ans


s="a+b*(c^d-e)"
k=infix_to_post(s)
print(k)