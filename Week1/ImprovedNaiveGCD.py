
#1.)WITH LISTS :
def naivegcd(m,n):
    res=[]
    for i in range(1,min(m,n)+1):
        if m%i==0 and n%i==0:
            res.append(i)
    return res[-1]
    #Aldready arranged in ascending so returning last element that is Greatest.
op = naivegcd(8,12)
print("GCD of 8 and 12 using lists is",op)
#Here the main approach is to scan in one go.
#Anyway the gcd is going to be one of two numbers min factor


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
