def fn(i):
    if i<1:
        return
    fn(i-1)
    print(i)
fn(3)
   
