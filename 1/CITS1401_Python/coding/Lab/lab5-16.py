def series(x):
    fun=x+1
    rr=0
    a=0
    while fun>=x:
        fun=1/(2**a)
        if fun < x:
            break
        rr+=fun
        a+=1
    return '{:.4f}'.format(rr)

print(series(0.5))
print(series(0.25))
print(series(0.05))
