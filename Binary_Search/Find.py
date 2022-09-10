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
