sumSquare = 0
squareSum = 0
for i in range(101):
    sumSquare += i**2
    squareSum += i 

squareSum **= 2

print(squareSum-sumSquare)