def isprime(num):
    if num<2:
        return False
    elif num <4:
        return True
    else:
        for den in range(2,num):
            if num % den ==0:
                return False
        return True

def primelist(N):
    plist=[]
    for num in range(N+1):
        if isprime(num):
            plist.append(num)
    return plist

def Nprimelist(N):
    count=0
    plist=[]
    while len(plist) <N:
        if isprime(count):
            plist.append(count)
        count +=1
    return plist

def Nprimelist(N):
    count=0
    plist=[]
    while True:
        if isprime(count):
            plist.append(count)
            if len(plist)>=N:
                break
        count +=1
    return plist

print(isprime(17))