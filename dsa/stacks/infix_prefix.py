def priority(s):
    if s=='^':
        return 3
    elif s=='*' or s=='/':
        return 2
    elif s=='+' or s=='-':
        return 1
    else:
        return 0
def reverse(s):
    s1=""
    for i in s[::-1]:
        if i=='(':
            s1=s1+')'
        elif i==')':
            s1=s1+'('
        else:
            s1=s1+i
    return s1
def infix_to_post(s):
    s=reverse(s)
    st=[]
    ans=""
   
    for i in s:
        if i.isalnum():
            ans=ans+i
        elif i=='(':
            st.append(i)
        elif i==')':
            while(not len(st)==0 and st[-1]!='('):
                ans=ans+st.pop()
            if st:st.pop()
        else:
            while(not len(st)==0 and priority(i)<priority(st[-1])):
               ans=ans+st[-1]
               st.pop()

            while(i=='^' and not len(st)==0 and priority(i)<=priority(st[-1])):
                ans=ans+st[-1]
                st.pop()
            st.append(i)
    while(not len(st)==0):
        ans=ans+st[-1]
        st.pop()
    return ans[::-1]


s="(a+b)*c-d+f"
k=infix_to_post(s)
print(k)