def Subset_Sum_Zero_One_Count(A, S, Mod = None):
    """ A の多重部分集合で, 和が s (0 <= s <= S) になる数を求める.

    Mod: 余り (None のときは余りを取らない)

    計算量: O(|A| S)
    """

    DP = [0] * (S + 1); DP[0] = 1

    for a in A:
        for x in range(S, a - 1, -1):
            DP[x] += DP[x - a]

        if Mod is not None:
            for x in range(a, S + 1):
                DP[x] %= Mod

    return DP

def Subset_Sum_Plus_Minus_One_Count(A, K, Mod = None):
    """ 以下を満たす A の分割 X, Y の個数を求める: sum(X) - sum(Y) = K.

    計算量: O(|A|(sum(A)+K))
    """

    A = list(map(abs, A))

    L = K + sum(A)
    if (L < 0) or (L % 2 == 1):
        return 0

    return Subset_Sum_Zero_One_Count(A, L // 2, Mod)[-1]
