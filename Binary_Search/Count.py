from bisect import bisect_left, bisect_right

def Binary_Search_Small_Count(A: list, x, equal = False, sort = False):
    """ 二分探索によって, A の元のうち, x より小さい元の個数を求める.

    Args:
        A (list): 探索対象のリスト
        x : 閾値
        equal (bool, optional): True のときは「x より小さい」が「x 以下」になる. Defaults to False.
        sort (bool, optional): A が昇順であることが保証されていないとき, True にすることで実行時にソートを行う. Defaults to False.

    Returns:
        int: x より小さい元の個数
    """
    if sort:
        A.sort()

    if equal:
        return bisect_right(A, x)
    else:
        return bisect_left(A, x)

def Binary_Search_Big_Count(A, x, equal = False, sort = False):
    """ 二分探索によって, A の元のうち, x より大きい元の個数を求める.

    Args:
        A (list): 探索対象のリスト
        x : 閾値
        equal (bool, optional): True のときは「x より大きい」が「x 以上」になる. Defaults to False.
        sort (bool, optional): A が昇順であることが保証されていないとき, True にすることで実行時にソートを行う. Defaults to False.

    Returns:
        int: x より大きい元の個数
    """

    if sort:
        A.sort()

    if equal:
        return len(A) - bisect_left(A, x)
    else:
        return len(A) - bisect_right(A, x)

def Binary_Search_Range_Count(A: list, x, y, left_equal = True, right_equal = True, sort = False):
    """ 二分探索によって, A に含まれる x 以上 y 以下の元の個数を求める.

    Args:
        A (list): 探索対象のリスト
        x : 下端の閾値
        y : 上端の閾値
        left_equal (bool, optional): False のときは「x 以上」が「x より大きい」になる. Defaults to True.
        right_equal (bool, optional): False のときは「y 以下」が「y より小さい」になる. Defaults to True.
        sort (bool, optional): A が昇順であることが保証されていないとき, True にすることで実行時にソートを行う. Defaults to False.

    Returns:
        int: x 以上 y 以下の元の個数
    """

    if sort:
        A.sort()

    alpha = Binary_Search_Small_Count(A, y, equal = right_equal)
    beta = Binary_Search_Small_Count(A, x, equal = not left_equal)
    return max(alpha - beta, 0)
