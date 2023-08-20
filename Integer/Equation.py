#拡張ユークリッドの互除法
def Find_Extend_Euclid(a: int, b: int, new = True):
    """ax+by=gcd(a, b) を満たす (x, y, gcd(a, b)) を 1 つ求める.
    a,b:整数
    """

    if new:
        from math import gcd
        g = gcd(a, b)
        if g == 0:
            return (1, 0, 0)

        x = pow(a//g, -1, b//g)
        y = - (a*x-g) // b
        return (x, y, g)
    else:
        s,t,u,v=1,0,0,1
        while b:
            q,a,b=a//b,b,a%b
            s,t=t,s-q*t
            u,v=v,u-q*v
        return s,u,a

def Solve_Bezout_Identity(a, b, c, lx, rx, ly, ry, extgcd = None):
    """ a x + b y = c , lx <= x <= rx, ly <= y <= ry を満たすような整数の組 (x,y) を求める.

    [Input]
    a != 0, b != 0
    lx <= rx, ly <= ry
    extgcd: (s,t) の形のタプルであり, a s + b t = gcd(a, b) でなくてはならない.

    [Output]
    存在しない場合, (None, None, None, None, None, None)
    存在する場合, (p0, p1, q0, q1, lk, rk) の形のタプルである. 以下を意味する.
    x = p0 + p1 k, y = q0 + q1 k, lk <= k <= rk
    """

    assert a != 0 and b != 0
    assert lx <= rx and ly <= ry

    if extgcd is None:
        s, t, g = Find_Extend_Euclid(a, b)
    else:
        s, t = extgcd
        g = a * s + b * t

    if c % g != 0:
        return (None, None, None, None, None, None)

    a //= g; b //= g; c //=g

    if b > 0:
        tmp_l = lx - c * s
        tmp_r = rx - c * s
    else:
        tmp_l = -(rx - c * s)
        tmp_r = -(lx - c * s)

    klx = (tmp_l + abs(b) - 1) // abs(b)
    krx = tmp_r // abs(b)

    if a > 0:
        tmp_l = -ry + c * t
        tmp_r = -ly + c * t
    else:
        tmp_l = -(-ly + c * t)
        tmp_r = -(-ry + c * t)

    kly = (tmp_l + abs(a) - 1) // abs(a)
    kry = tmp_r // abs(a)


    kl = max(klx, kly); kr = min(krx, kry)
    if kl > kr:
        return (None, None, None, None, None, None)

    return (c * s, b, c * t, -a, kl, kr)

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
