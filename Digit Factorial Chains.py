data = [0]*1000000

def fact(k):
    if k == 0:
        return 1
    
    final = 1
    for i in range(1,k+1):
        final*=i
    return final

factorial = [fact(k) for k in range(10)]

def operate(num):   
    final = 0
    for i in str(num):
        final+=factorial[int(i)]
    return final

for i in range(1,1000000):
    count = 0
    current = i
    const = i
    chain = [0,0,current]
    while(True):
        new = operate(current)
        chain.append(new)
        current = new
        if chain[-1] == chain [-2]:
            data[const] = len(chain)-1
            break
        if chain[-1] == chain [-3]:
            data[const] = len(chain)-2
            break
        if chain[-1] == chain [-4]:
            data[const] = len(chain)-3
            break
        
final = 0
for i in data:
    if i == 60:
        final+=1

print(final)