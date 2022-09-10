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
