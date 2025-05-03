from implementation_using_list import Stack

def is_balanced(s1):
    s = Stack()
    for i in s1:
        if i in '[{(':
            s.push(i)
        else:
            if s.is_empty():
                return False
            char = s.pop()
            if char == '[' and i != ']':
                return False
            if char == '(' and i != ')':
                return False
            if char == '{' and i != '}':
                return False
    return s.is_empty()

s1 = "{[()]}"
print(is_balanced(s1))  
