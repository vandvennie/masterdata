l= list(range(10))
print(l)
m=map(lambda x: x**2,[1])
print(list(m))
t=[('Fred',55), ('Jemima',68), ('James',45)]
t.sort(key=lambda x:x[1])
print(t)
                                
d={1:"alan",2:"chris",3:"sara"}
print(d[2])

d["default"]="No name is stored"
print(d[2])
d.get(1,"No name is stored")

a={1,2,2,3}
print(a)