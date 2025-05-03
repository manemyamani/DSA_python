k=0
for i in range(0,5):
    for j in range(5,i,-1):
        g=chr(65+k)
        k=k+1
        print(g,end="")
    print()