def Find_Previous_Arithmetic_Progression(l: int, d: int, k: int, x: int, default = None):
    """ 初項 l, 公差 d, 項数 k の整数列にある x 以下の最大の項を求める.

    Args:
        l (int): 初項
        d (int): 公差
        k (int): 項数
        x (int): 下端
        default : 存在しない場合の返り値. Defaults to None.
    """

    if d < 0:
        l, d = l + (k - 1) * d, -d

    if d == 0:
        return x if x == l else default

    r = l + (k - 1) * d
    if x < l:
        return default

    x = min(x, r)
    p = (x - l) // d
    return l + p * d

def Find_Next_Arithmetic_Progression(l: int, d: int, k: int, x: int, default = None):
    """ 初項 l, 公差 d, 項数 k の整数列にある x 以上の最小の項を求める.

    Args:
        l (int): 初項
        d (int): 公差
        k (int): 項数
        x (int): 下端
        default : 存在しない場合の返り値. Defaults to None.
    """

    if d < 0:
        l, d = l + (k - 1) * d, -d

    if d == 0:
        return x if x == l else default

    r = l + (k - 1) * d
    if r < x:
        return default

    x = max(x, l)
    p = (x - l + d - 1) // d
    return l + p * d
