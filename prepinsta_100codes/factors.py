for i in range(1,10):
    li=[]
    for j in range(1,i+1):
        if i%j==0:
            li.append(j)
    print("the factors of" ,i ," are:",li)
        
