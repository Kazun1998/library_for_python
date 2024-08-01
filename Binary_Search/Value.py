from bisect import bisect_left, bisect_right

def Binary_Search_Low_Value(A: list, x, equal = False, default = None, sort = False):
    """ 二分探索によって, A の元のうち, x 未満の要素のうち最大の要素を求める.

    Args:
        A (list): 探索対象のリスト
        x : 閾値
        equal (bool, optional): True のときは「x 未満」が「x 以下」になる. Defaults to False.
        default (optional): A の全ての要素が x 以上 (より大きいとき) の返り値. Defaults to None.
        sort (bool, optional): A が昇順であることが保証されていないとき, True にすることで実行時にソートを行う. Defaults to False.
    """

    if sort:
        A.sort()

    if equal:
        ind = bisect_right(A, x)
    else:
        ind = bisect_left(A, x)

    return A[ind - 1] if ind > 0 else default

def Binary_Search_High_Value(A, x, equal = False, default = None, sort = False):
    """ 二分探索によって, A の元のうち, x より大きいの要素のうち最大の要素を求める.

    Args:
        A (list): 探索対象のリスト
        x : 閾値
        equal (bool, optional): True のときは「x より大きい」が「x 以上」になる. Defaults to False.
        default (optional): A の全ての要素が x 以下 (未満) の返り値. Defaults to None.
        sort (bool, optional): A が昇順であることが保証されていないとき, True にすることで実行時にソートを行う. Defaults to False.
    """

    if sort:
        A.sort()

    if equal:
        ind = bisect_left(A, x)
    else:
        ind = bisect_right(A, x)

    return A[ind] if ind < len(A) else default

def Binary_Search_High_Low_Value(A: list, x, low_equal = False, high_equal = False, low_default = None, high_default = None, sort = False):
    """ 二分探索によって, A の x 未満で最大の要素 p と x より大きい最小の要素 q を求め, (p, q) を出力する.

    Args:
        A (list): 捜索対象のリスト
        x : 閾値
        low_equal (bool, optional): True のときは「x 未満」が「x 以下」になる. Defaults to False.
        high_equal (bool, optional):  True のときは「x より大きい」が「x 以上」になる. Defaults to False.
        low_default (optional): A の全ての要素が x 以上 (より大きいとき) の返り値. Defaults to None.
        high_default (optional): A の全ての要素が x 以下 (未満) の返り値. Defaults to None.
        sort (bool, optional): A が昇順であることが保証されていないとき, True にすることで実行時にソートを行う. Defaults to False.

    Returns:
        (p, q): p: A の x 未満で最大の要素, q: x より大きい最小の要素
    """

    if sort:
        A.sort()

    return (
        Binary_Search_Low_Value(A, x, equal = low_equal, default = low_default),
        Binary_Search_High_Value(A, x, equal = high_equal, default = high_default)
        )
