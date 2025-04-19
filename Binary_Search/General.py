def General_Binary_Increase_Search_Integer(L: int, R: int, cond, default = None) -> int:
    """ 条件式が単調増加であるとき, 整数上で二部探索を行い, cond(x) が真になる最小の整数 x を求める.

    Args:
        L (int): 解の下限
        R (int): 解の上限
        cond (Callable[[int], bool]): 条件(1変数関数, 広義単調増加を満たす)
        default (Any, optional): R で条件を満たさない (つまり, [L, R] 上では常に偽) ときの返り値. Defaults to None.

    Returns:
        int: cond(x) が真になる最小の整数 x
    """
    if not cond(R):
        return default

    if cond(L):
        return L

    R += 1
    while R - L>1:
        C = L + (R - L) // 2
        if cond(C):
            R = C
        else:
            L = C
    return R

def General_Binary_Decrease_Search_Integer(L: int, R: int, cond, default = None) -> int:
    """ 条件式が単調減少であるとき, 整数上で二部探索を行い, cond(x) が真になる最大の整数 x を求める.

    Args:
        L (int): 解の下限
        R (int): 解の上限
        cond (Callable[[int], bool]): 条件(1変数関数, 広義単調減少を満たす)
        default (Any, optional): L で条件を満たさない (つまり, [L, R] 上では常に偽) ときの返り値. Defaults to None.

    Returns:
        int: cond(x) が真になる最小の整数 x
    """

    if not cond(L):
        return default

    if cond(R):
        return R

    L -= 1
    while R - L > 1:
        C = L + (R - L) // 2
        if cond(C):
            L = C
        else:
            R = C
    return L

def General_Binary_Increase_Search_Real(L: float, R: float, cond, trial: int, default: float = None) -> float:
    """ 条件式 cond が単調増加であるとき, 実数上での cond に関する二分探索を行い, cond(x) が真になる最小の実数 x の近似値を求める.

    Args:
        L (float): 下限
        R (float): 上限
        cond (Callable[[float], bool]): 条件式 (単調増加)
        trial (int): 判定回数の最大値
        default (float, optional): cond(R) が偽になるときの返り値. Defaults to None.

    Returns:
        float: cond(x) が最小になる実数 x の近似値
    """

    # [L, R] で挟めない場合を先に処理する.
    if not cond(R):
        return default

    if cond(L):
        return L

    for _ in range(trial):
        C = L + (R - L) / 2
        if cond(C):
            R = C
        else:
            L = C

    return (L + R) / 2

def General_Binary_Decrease_Search_Real(L: float, R: float, cond, trial: int, default: float = None) -> float:
    """ 条件式 cond が単調減少であるとき, 実数上での cond に関する二分探索を行い, cond(x) が真になる最大の実数 x の近似値を求める.

    Args:
        L (float): 下限
        R (float): 上限
        cond (Callable[[float], bool]): 条件式 (単調増加)
        trial (int): 判定回数の最大値
        default (float, optional): cond(L) が偽になるときの返り値. Defaults to None.

    Returns:
        float: cond(x) が最大になる実数 x の近似値
    """

    # [L, R] で挟めない場合を先に処理する.

    if not cond(L):
        return default

    if cond(R):
        return R

    for _ in range(trial):
        C = L + (R - L) / 2
        if cond(C):
            L = C
        else:
            R = C

    return (L + R) / 2
