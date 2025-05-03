def fn(n):
    if n==0:
        return 0
    return fn(n-1)+n
print(fn(3))