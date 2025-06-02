x = 1000000*2

primes = {i:1 for i in range(2,x+1)}

for i in range(2,x+1):
    if primes[i] == 1:
        cur = i
        ind = 2
        while(cur*ind<x+1):
            primes[cur*ind] = 0
            
            ind+=1

sum = 0
for key in primes.keys():
    if primes[key]==1:
        sum+=key
print(sum)