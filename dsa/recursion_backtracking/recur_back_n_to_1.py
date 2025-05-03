def fn(i,n): #functional recursion
    if i>n:
        return
    fn(i+1,n)
    print(i)
fn(1,5)