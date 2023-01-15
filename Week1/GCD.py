def gcd(m,n):
    l=[]
    p=[]
    res=[]
    for i in range(1,m+1):
        if m%i==0:
            l.append(i)
    for i in range(1,n+1):
        if n%i==0:
            p.append(i)
    for i in l:
        if i in p:
            res.append(i)
    return res[-1]
op=gcd(6,8)
print("GCD is",op)
#Factors of 6=1,2,3,6
#Factors of 8=1,2,4,8
#GCD of 6 and 8 = 2.
