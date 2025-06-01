from math import sqrt,floor

for a in range(1,1000):
    for b in range(a,1000):
        sqr = floor(sqrt(a**2+b**2))
        if (a**2+b**2)%sqr == 0 and a+b+sqr==1000:
            print(a,b,sqr)
