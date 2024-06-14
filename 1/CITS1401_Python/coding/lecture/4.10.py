def add(balances,rate):
    for idx in range(len(balances)):
        newbalance =balances[idx]*(1+rate)
        balances[idx]=newbalance
    return balances
ca=[1000,2000,2500,3000,10000]
r=0.1
nc=add(ca,r)
print(nc)
print(ca)