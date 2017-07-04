def gcd(a,b):
    if(a>b):
        c = a%b
        if (c==0):
            return b
        else:
            return gcd(c,b)
    else:
        c = b%a
        if (c==0):           
            return a
        else:
            return gcd(c,a)

value = gcd(120,75)
print('gcd(120,75) =', value)