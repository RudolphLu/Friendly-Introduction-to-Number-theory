#
# Quick solution from linear function
# ax+by =gcd(a,b)
#

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
			
v_g = v_x = v_y = 0
[v_g,v_x,v_y] = linear_equation(67890,12345)
print('gcd(12345,67890) =', v_g,v_x,v_y)