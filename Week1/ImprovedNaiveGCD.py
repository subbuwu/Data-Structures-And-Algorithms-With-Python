
#1.)WITH LISTS :
def naivegcd(m,n):
    res=[]
    for i in range(1,min(m,n)+1):
        if m%i==0 and n%i==0:
            res.append(i)
    return res[-1]
op = naivegcd(8,12)
print("GCD of 8 and 12 using lists is",op)
#Here the main approach is to scan in one go.
#8=1,2,4,8 || 12=1,2,3,4,6,12
#Anyway the gcd is going to be one's min factor


#2.)WITHOUT LISTS :
def gcd(m,n):
    mcf=0
    for i in range(1,min(m,n)+1):
        if m%i==0 and n%i==0:
            mcf=i
        #It takes the factor and at last stores the greatest in mcf variable
    return mcf
op = gcd(8,12)
print("GCD of 8 and 12 wihtout using lists is",op)