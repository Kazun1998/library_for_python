#最小公倍数
def lcm(m,n):
    from math import gcd
    return (m//gcd(m,n))*n

def LCM(*X):
    from functools import reduce
    return reduce(lcm,X)

#floor(a^(1/k)) を求める.
def Floor_Root(a,k):
    """floor(a^(1/k)) を求める.

    a:非負整数
    k:正の整数
    """
    assert 0<=a and 0<k
    if a==0: return 0
    if k==1: return a

    #大体の値を求める.
    x=int(pow(a,1/k))

    #増やす
    while pow(x+1,k)<=a:
        x+=1

    #減らす
    while pow(x,k)>a:
        x-=1
    return x

#ceil(a^(1/k)) を求める.
def Ceil_Root(a,k):
    """ceil(a^(1/k)) を求める.

    a:非負整数
    k:正の整数
    """
    assert 0<=a and 0<k
    if a==0:
        return 0
    if k==1:
        return a

    #大体の値を求める.
    x=int(pow(a,1/k))+1

    #増やす
    while pow(x,k)<a:
        x+=1

    #減らす
    while a<=pow(x-1,k):
        x-=1
    return x

def kth_Power(a,k):
    """ 整数 a が k 乗数かどうかを求め, そうならば, b^k=a を満たす k を返す.

    [Input]
    a: int
    k: int (k>0)

    [Output]
    存在しない  : None
    存在する    : b^k=a を満たす b
    """

    if k%2==0:
        if a<0:
            return None
        b=Floor_Root(a,k)
        return b if pow(b,k)==a else None
    else:
        sgn=1 if a>=0 else -1
        b=Floor_Root(abs(a),k)
        return sgn*b if pow(sgn*b,k)==a else None

#===
def Integer_Equation(P, Y, L=0, default=None):
    """ P[0]+P[1]x+...+P[n-1]x^(n-1)=Y を満たす整数 x を求める.

    P: 多項式 (1次以上, 非零であり, L<=x の範囲で P は単調増加でなくてはならない).
    Y: int
    L: int (x としてありうる下界を求める).
    default: 存在しない場合の返り値
    """

    P=list(P)
    while P and P[-1]==0:
        P.pop()
    assert len(P)>=2

    def calc(x):
        y=0
        for p in reversed(P):
            y=(y*x+p)
        return y

    if calc(L)>Y:
        return default

    # 上界を求める
    d=1
    while calc(L+d)<=Y:
        d*=2
    R=L+d

    # 解を求める
    while R-L>1:
        C=L+(R-L)//2
        if calc(C)<=Y:
            L=C
        else:
            R=C
    return L if calc(L)==Y else default

def Integer_Inequality(P, Y, L=0, mode=True, default=None):
    """ P[0]+P[1]x+...+P[n-1]x^(n-1) <= Y を満たす最大の整数 x を求める.

    P: 多項式 (1次以上, 非零であり, L<=x の範囲で P は単調増加でなくてはならない).
    Y: int
    L: int (x としてありうる下界を求める).
    mode: True の場合は <=, False の場合は < になる.
    default: 存在しない場合の返り値
    """

    P=list(P)
    while P and P[-1]==0:
        P.pop()
    assert len(P)>=2

    def calc(x):
        y=0
        for p in reversed(P):
            y=(y*x+p)
        return y

    if calc(L)>Y or (not mode and calc(L)==Y):
        return default

    # 上界を求める
    d=1
    if mode:
        while calc(L+d)<=Y:
            d*=2
    else:
        while calc(L+d)<Y:
            d*=2
    R=L+d

    # 解を求める
    while R-L>1:
        C=L+(R-L)//2
        y0=calc(C)
        if y0<Y or (mode and y0==Y):
            L=C
        else:
            R=C
    return L
