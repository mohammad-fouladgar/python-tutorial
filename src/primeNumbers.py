import time
import math

def isPrime(n): 
    if(n<=1):
        return False
    if(n==2):
        return True
    
    if( n > 2 and n % 2==0):
        return False

    max_div = math.floor(math.sqrt(n))

    for i in range(3,1+max_div,2):
        if(n % i==0):
            return False
    print(n,' is prime')
    return True

c = 0 #for counting 
t0 = time.time() 
# Driver Program 
for n in range(1,100000):
    x= isPrime(n)
    c+=x

t1 = time.time() 	

print("Time required :", t1 - t0)

print("Total prime numbers in range :", c) 

