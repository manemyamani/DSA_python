import math #forelse
primes=[]
for num in range(2,20):
    for i in range(2,math.isqrt(num)+1):
        if num%i==0:
            break
    else:
        primes.append(num)
        
print(primes)


