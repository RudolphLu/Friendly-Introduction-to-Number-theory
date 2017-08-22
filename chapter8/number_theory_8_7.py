#
# Find all incongruent solutions
#
# ax congruent c to m
#    ax = c (mod m).

def linear_equation(a,b):
    g = a
    w = b
    x = 1
    v = 0
    def sub_linear(x,g,v,w):
        if(w==0):
            y = (g-a*x)//b
            return [g,x,y]
        else:
            q=g//w 
            t=g%w
            s=x-q*v
            return sub_linear(v,w,s,t)
    return sub_linear(x,g,v,w)

X = 2432
Y = 893
    
div = v_g = v_x = v_y = 0
[v_g,v_x,v_y] = linear_equation(X,Y)

c = 266 

#above this case v_x -> negative
#                v_y -> postive

modX = Y//v_g;
modY = X//v_g;

while(v_x>0 or v_y<0):
    v_x = v_x-modX
    v_y = v_y+modY

print('gcd(2432,893) =', v_g,v_x,v_y)    
    
if(c%v_g == 0):
    div = c//v_g;
    v_x = v_x * div;
    v_y = v_y * div
    print('first congruent solution =', -v_x,v_y)
else:
    print('No congruent solutions')


