def Longest_Increasing_Subsequence(A: list, equal = False) -> dict:
    """ A に対する LIS (最大狭義単調増加列) を求める

    Args:
        A (list): 列
        equal (bool, optional): True にすると, LIS の条件が最大広義単調増加列になる. Defaults to False.

    Returns:
        dict:
            length: 最大単調増加列の長さ
            example: 最大単調増加列の例
            index: example においてそれぞれの項を持ってきたインデックス
    """
    if equal:
        from bisect import bisect_right as bis
    else:
        from bisect import bisect_left as bis

    L = []
    ind = [0] * len(A)

    for i, a in enumerate(A):
        k = bis(L, a)
        if k == len(L):
            L.append(a)
        else:
            L[k] = a

        ind[i] = k

    LIS = []
    I = []
    j = len(L)-1
    for i in range(len(A) - 1, -1, -1):
        if ind[i] != j:
            continue

        j -= 1
        LIS.append(A[i])
        I.append(i)

    LIS.reverse()
    I.reverse()

    return { 'length': len(LIS), 'example': LIS, 'index': I }