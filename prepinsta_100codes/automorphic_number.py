for i in range(1,100):
    k=(i*i)%pow(10,len(str(i)))
    if i==k:
        print(i,"is automorphic number")