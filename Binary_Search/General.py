def General_Binary_Increase_Search_Integer(L, R, cond, default=None):
    """ 条件式が単調増加であるとき, 整数上で二部探索を行う.

    L: 解の下限
    R: 解の上限
    cond: 条件(1変数関数, 広義単調増加を満たす)
    default: Lで条件を満たさないときの返り値
    """

    if not(cond(R)):
        return default

    if cond(L):
        return L

    R+=1
    while R-L>1:
        C=L+(R-L)//2
        if cond(C):
            R=C
        else:
            L=C
    return R

def General_Binary_Decrease_Search_Integer(L, R, cond, default=None):
    """ 条件式が単調減少であるとき, 整数上で二部探索を行う.

    L: 解の下限
    R: 解の上限
    cond: 条件 (1変数関数, 広義単調減少 を満たす)
    default: R で条件を満たさないときの返り値
    """

    if not(cond(L)):
        return default

    if cond(R):
        return R

    L-=1
    while R-L>1:
        C=L+(R-L)//2
        if cond(C):
            L=C
        else:
            R=C
    return L

def General_Binary_Increase_Search_Real(L, R, cond, ep, Times, default=None):
    """ 条件式が単調増加であるとき, 実数上で一般的な二部探索を行う.

    L: 解の下限
    R: 解の上限
    cond: 条件(1変数関数, 広義単調増加を満たす)
    ep: 解の許容する誤差
    Times: 判定回数の上限
    default: Lで条件を満たさないときの返り値
    """
    if not(cond(R)):
        return default

    if cond(L):
        return L

    while (R-L)>=ep or Times:
        Times-=1
        C=L+(R-L)/2
        if cond(C):
            R=C
        else:
            L=C
    return (L+R)/2

def General_Binary_Decrease_Search_Real(L, R, cond, ep, Times, default=None):
    """ 条件式が単調減少であるとき, 実数上で一般的な二部探索を行う.

    L:解の下限
    R:解の上限
    cond:条件(1変数関数, 広義単調減少を満たす)
    ep: 解の許容する誤差
    Times: 判定回数の上限
    default: Rで条件を満たさないときの返り値
    """

    if not(cond(L)):
        return default

    if cond(R):
        return R

    while (R-L)>=ep or Times:
        Times-=1
        C=L+(R-L)/2
        if cond(C):
            L=C
        else:
            R=C
    return (L+R)/2
