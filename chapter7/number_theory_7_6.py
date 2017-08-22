#
# 
# Find all primes factors
#
import numpy

g_matrix_2d = {}

def factorize_integer(a):
    min_factor=2
    max_factor=int(numpy.sqrt(a))
    match = 0
    for num in range(min_factor,max_factor):
        b = a % num
        if(b==0):
            match = 1
            c = a//num
            if(num in g_matrix_2d):
                g_matrix_2d[num]+=1
            else:
                g_matrix_2d[num]=1
            factorize_integer(c)
            break
    if(match!=1):
        if(a in g_matrix_2d):
            g_matrix_2d[a]+=1
        else:
            g_matrix_2d[a]=1
                        
factorize_integer(75460)
dict(g_matrix_2d)
print("full:",g_matrix_2d)
