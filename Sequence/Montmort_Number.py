def Montmort_Number(N: int, Mod: int = None) -> list[int]:
    """ k = 0, 1, 2, ..., N に対して, k 要素撹乱順列の個数 (を Mod で割った余り) を求める.

    Args:
        N (int): 求める k の上限
        Mod (int, optional): 整数を設定すると, 各値は個数を Mod で割った余りになる. Defaults to None.

    Returns:
        list[int]: 長さ (N + 1) のリスト. 第 k 要素は k 要素撹乱順列の個数 (を Mod で割った余り) である.
    """

    if N < 0:
        return []
    elif N == 0:
        return [0]

    dp = [0] * (N + 1)
    if Mod is None:
        for k in range(2, N + 1):
            dp[k] = k * dp[k - 1] + (-1 if k % 2 else 1)
    else:
        for k in range(2, N+1):
            dp[k] = (k * dp[k - 1] + (-1 if k % 2 else 1)) % Mod

    return dp
