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
    return max(alpha-beta,0)
