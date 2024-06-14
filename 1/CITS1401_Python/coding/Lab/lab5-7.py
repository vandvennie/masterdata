def sequence(n):
    li=[]
    while n!=1:
        if n%2==0:
            li.append(int(n))
            n=n/2
        else:
            li.append(int(n))
            n=3*n+1
    li.append(int(n))
    return li

print(sequence(12))
print(sequence(20))

