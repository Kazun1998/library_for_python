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
