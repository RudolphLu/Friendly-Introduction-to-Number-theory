def gcd(a,b):
    if(a>b):
        c = a%b
        print("(a,b,c,d)",a,b,c,a/b);
        if (c==0):
            return b
        else:
            return gcd(c,b)
    else:
        c = b%a
        print("(a,b,c,d)",a,b,c,b/a);
        if (c==0):           
            return a
        else:
            return gcd(c,a)

value = gcd(12345,67890)
print('gcd(12345,67890) =', value)
