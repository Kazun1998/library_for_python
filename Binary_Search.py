def Binary_Search_Find(A, x, sort=False):
    """ 二分探索によって, A に x が存在するかどうかを調べる.

    A: リスト
    x: 調べる要素
    sort: ソートをする必要があるかどうか(Trueで必要)
    """
    if sort:
        A.sort()

    if len(A)==0 or x<A[0] or A[-1]<x:
        return False

    L,R=0,len(A)
    while R-L>0:
        C=L+(R-L)//2
        if x<A[C]:
            R=C
        elif x>A[C]:
            L=C+1
        else:
            return True
    return False

def Binary_Search_Index(A, x, sort=False, default=None, offset=0):
    """ 二分探索によって, A に x が存在するれば, そのインデックスを返す.
    (x が複数ある時, 返ってくるインデックスは不定)

    A: リスト
    x: 調べる要素
    sort: ソートをする必要があるかどうか (True で必要)
    default: 存在しなかった場合の返り値
    offset=0: インデックス+ offset の値を返す.
    """
    if sort:
        A.sort()

    if len(A)==0 or x<A[0] or A[-1]<x:
        return default

    L,R=0,len(A)
    while R-L>0:
        C=L+(R-L)//2
        if x<A[C]:
            R=C
        elif x>A[C]:
            L=C+1
        else:
            return C+offset
    return default

def Binary_Search_Small_Count(A, x, equal=False, sort=False):
    """二分探索によって, x 未満の要素の個数を調べる.

    A: リスト
    x: 調べる要素
    sort: ソートをする必要があるかどうか (True で必要)
    equal: True のときは x "未満" が x "以下" になる
    """
    if sort:
        A.sort()

    if len(A)==0 or A[0]>x or ((not equal) and A[0]==x):
        return 0

    L,R=0,len(A)
    while R-L>1:
        C=L+(R-L)//2
        if A[C]<x or (equal and A[C]==x):
            L=C
        else:
            R=C

    return L+1

def Binary_Search_Big_Count(A, x, equal=False, sort=False):
    """二分探索によって, x を超える要素の個数を調べる.

    A: リスト
    x: 調べる要素
    sort: ソートをする必要があるかどうか (True で必要)
    equal: True のときは x "を超える" が x "以上" になる
    """

    if sort:
        A.sort()

    if len(A)==0 or A[-1]<x or ((not equal) and A[-1]==x):
        return 0

    L,R=-1,len(A)-1
    while R-L>1:
        C=L+(R-L)//2
        if A[C]>x or (equal and A[C]==x):
            R=C
        else:
            L=C
    return len(A)-R

def Binary_Search_Range_Count(A, x, y, sort=False, left_close=True, right_close=True):
    """二分探索によって, x 以上 y 以下 の個数を調べる.

    A: リスト
    x, y: 調べる要素
    sort: ソートをする必要があるかどうか (True で必要)
    left_equal: True のときは x<=a, False のときは x<a
    right_equal: True のときは y<=a, False のときは y<a
    """

    if sort:
        A.sort()

    alpha=Binary_Search_Small_Count(A, y, equal=right_close)
    beta =Binary_Search_Small_Count(A, x, equal=not left_close)
    return alpha-beta

def Binary_Search_Low_Value(A, x, equal=False, sort=False, default=None):
    """ A の x 未満の要素の中で最大のものを出力する.

    A: リスト
    x: 調べる要素
    sort: ソートをする必要があるかどうか (True で必要)
    equal: True のときは x "未満" が x "以下" になる
    ※ 全ての要素が x 以上 (超える) 場合は default が返される.
    """

    if sort:
        A.sort()

    if len(A)==0 or A[0]>x or ((not equal) and A[0]==x):
        return default

    L,R=0,len(A)
    while R-L>1:
        C=L+(R-L)//2
        if A[C]<x or (equal and A[C]==x):
            L=C
        else:
            R=C

    return A[L]

def Binary_Search_High_Value(A, x, equal=False, sort=False, default=None):
    """ A の x を超える要素の中で最小のものを出力する.

    A: リスト
    x: 調べる要素
    sort: ソートをする必要があるかどうか (True で必要)
    equal: True のときは x "を超える" が x "以上" になる
    ※ 全ての要素が x 以上 (を超える) 場合は default が返される.
    """

    if sort:
        A.sort()

    if len(A)==0 or A[-1]<x or ((not equal) and A[-1]==x):
        return default

    L,R=-1,len(A)-1
    while R-L>1:
        C=L+(R-L)//2
        if A[C]>x or (equal and A[C]==x):
            R=C
        else:
            L=C
    K=len(A)-R
    return A[-K]

def Binary_Search_High_Low_Value(A, x, low_equal=False, high_equal=False, sort=False, low_default=None, high_default=None):
    """ Aの x 未満で最大の要素 p と x を超える最小の要素 q を見つけ, (p,q) を出力する.

    A: リスト
    x: 調べる要素
    sort: ソートをする必要があるかどうか (True で必要)
    low_equal: True のときは x "未満" が x "以下" になる
    high_equal: True のときは x "を超える" が "以上" になる
    """

    if sort:
        A.sort()

    return (
        Binary_Search_Low_Value(A,x,equal=low_equal,default=low_default),
        Binary_Search_High_Value(A,x,equal=high_equal,default=high_default)
        )

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

def General_Binary_Increase_Search_Real(L, R, cond,ep=1/(1<<20), Times=50, default=None):
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

    while (R-L)>=ep and Times:
        Times-=1
        C=L+(R-L)/2
        if cond(C):
            R=C
        else:
            L=C
    return (L+R)/2

def General_Binary_Decrease_Search_Real(L, R, cond, ep=1/(1<<20), Times=50, default=None):
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

    while (R-L)>=ep and Times:
        Times-=1
        C=L+(R-L)/2
        if cond(C):
            L=C
        else:
            R=C
    return (L+R)/2

def Ternary_Search_Minimize(L, R, f, Integer=True, arg=False, ep=1/(1<<20), Times=50):
    """ 三部探索による最小値を求める.

    f: [L,R] 内で下に凸または単調減少
    """
    if Integer:
        while (R-L)>3:
            a=(2*L+R)//3
            b=(L+2*R)//3
            p=f(a);q=f(b)
            if p<=q: R=b
            else: L=a

        a=(2*L+R)//3
        b=(L+2*R)//3
    else:
        while (R-L)>=ep and Times:
            Times-=1
            a=(2*L+R)/3
            b=(L+2*R)/3

            p=f(a);q=f(b)
            if p<=q: R=b
            else: L=a

        a=(2*L+R)/3
        b=(L+2*R)/3

    if arg:
        y=float("inf")
        argx=-1
        for x in [L,a,b,R]:
            p=f(x)
            if y>p:
                y=p
                argx=x
        return y,argx
    else:
        return min(f(L),f(a),f(b),f(R))

def Ternary_Search_Maximize(L, R, f, Integer=True, arg=False, ep=1/(1<<20), Times=50):
    """ 三部探索による最大値を求める.

    f: [L,R] 内で上に凸または単調増加
    """
    if Integer:
        while (R-L)>3:
            a=(2*L+R)//3
            b=(L+2*R)//3
            p=f(a);q=f(b)
            if p>=q: R=b
            else: L=a

        a=(2*L+R)//3
        b=(L+2*R)//3
    else:
        while (R-L)>=ep and Times:
            Times-=1
            a=(2*L+R)/3
            b=(L+2*R)/3

            p=f(a);q=f(b)
            if p>=q: R=b
            else: L=a

        a=(2*L+R)/3
        b=(L+2*R)/3

    if arg:
        y=-float("inf")
        argx=-1
        for x in [L,a,b,R]:
            p=f(x)
            if y<p:
                y=p
                argx=x
        return y,argx
    else:
        return min(f(L),f(a),f(b),f(R))
