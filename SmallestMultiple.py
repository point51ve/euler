num = 1
k = 20
primes = [2,3,5,7,11,13,17,19]
def primeDecomp(j):
    decomp = {p:0 for p in primes}
    for i in primes:
        copy = j
        while copy%i == 0:
            decomp[i]+=1
            copy//=i
    return decomp

for i in range(1,k+1):
    numDecomp = primeDecomp(num)
    pDecomp = primeDecomp(i)
    newDict = {p:0 for p in primes}

    for p in primes:
        newDict[p] = max(numDecomp[p],pDecomp[p])
    num = 1
    for p in primes:
        num *=p**(newDict[p])

print(num)
