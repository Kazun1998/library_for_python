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
