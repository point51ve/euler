def checkPalindrome(str):
    for i in range(len(str)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

print(checkPalindrome("9119"))

maximum = 0
for i in range(100,1000):
    for j in range(100,1000):
        num = i*j
        if checkPalindrome(str(num)) and num>maximum:
            maximum = num

print(maximum)