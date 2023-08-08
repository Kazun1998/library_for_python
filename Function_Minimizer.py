def Quadratic_Function_Minimize(a,b,c,l,r):
    """ l<=x<=r における ax^2+bx+c の最小値を求める.
    """

    f=lambda x:x*(a*x+b)+c

    if a==0:
        return min(f(l),f(r))
    elif a>0:
        xi=-b/(2*a)
        if l<=xi<=r:
            x=xi
        elif r<=xi:
            x=r
        else:
            x=l
        return f(x)
    else:
        return min(f(l), f(r))

def Quadratic_Function_Maximize(a,b,c,l,r):
    """ l<=x<=r における ax^2+bx+c の最大値を求める.
    """

    return -Quadratic_Function_Minimize(-a,-b,-c,l,r)

def Quadratic_Function_Minimize_Integer(a,b,c,l,r):
    """ l<=x<=r , x:整数 における ax^2+bx+c の最小値を求める.
    """

    f=lambda x:x*(a*x+b)+c

    if a==0:
        return min(f(l),f(r))
    elif a>0:
        if 2*a*l<=-b<=2*a*r:
            x=(a-b)//(2*a)
        elif 2*a*r<=-b:
            x=r
        else:
            x=l
        return f(x)
    else:
        return min(f(l), f(r))

def Quadratic_Function_Maximize_Integer(a,b,c,l,r):
    """ l<=x<=r における ax^2+bx+c の最大値を求める.
    """

    return -Quadratic_Function_Minimize_Integer(-a,-b,-c,l,r)

#=================================================
def Linear_Inverse_Sum_Function_Minimize(a,b,c,l,r):
    """ l<=x<=r における ax+b/x+c の最小値を求める.
    """

    f=lambda x:a*x+b/x+c

    if a==0:
        return f(r)
    elif b==0:
        return f(l)

    from math import sqrt
    x=sqrt(b/a)

    if l<=x<=r:
        return f(x)
    elif r<=x:
        return f(r)
    else:
        return f(l)

def Linear_Inverse_Sum_Function_Minimize_Integer(a,b,c,l,r):
    """ l<=x<=r, x: 整数 における ax+b/x+c の最小値を求める.
    """

    f=lambda x:a*x+b/x+c

    if a==0:
        return b//r+c
    elif b==0:
        return a*l+c

    if r*r<=b//a:
        return f(r)
    elif (b+a-1)//a<=l*l:
        return f(l)
    else:
        p=b//a
        x=int(pow(p,1/2))

        while (x+1)*(x+1)<=p:
            x+=1

        while x*x>p:
            x-=1

        if x==0:
            return f(1)
        else:
            return min(f(x), f(x+1))
