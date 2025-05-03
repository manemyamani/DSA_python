def gcd(div1,div2):
    k=div2%div1
    if k==0:
        return div1
    else:
        return gcd(k,div1)
print(gcd(17,19))