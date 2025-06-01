from math import sqrt,ceil

number = 600851475143

x = 775147*2
primes = {i:1 for i in range(2,x+1)}

for i in range(2,x+1):
    if primes[i] == 1:
        cur = i
        ind = 2
        while(cur*ind<x+1):
            primes[cur*ind] = 0
            
            ind+=1

maximum = 0

for num in primes.keys():
    if primes[num] == 1:
        maximum +=1
        if maximum == 10001:
            print(num)

print(maximum)

    

