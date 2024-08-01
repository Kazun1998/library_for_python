def Subset_Sum_Zero_One_Find(A, S):
    """ A の多重部分集合で, 和が S になる (0, 1) 列の例を求める.

    計算量: O(|A| S)
    """

    N = len(A)
    DP = [[False]* (S + 1) for _ in range(N + 1)]; DP[0][0] = True

    for i, a in enumerate(A, 1):
        DP_i = DP[i]; DP_prev = DP[i - 1]
        for x in range(S, a - 1, -1):
            DP_i[x] = DP_prev[x] | DP_prev[x - a]
        for x in range(a - 1, -1, -1):
            DP_i[x] = DP_prev[x]

    if not DP[N][S]:
        return None

    signs = []
    pointer = S
    for i, a in reversed(list(enumerate(A, 1))):
        DP_prev = DP[i - 1]
        if (pointer >= a) and DP_prev[pointer - a]:
            signs.append(1)
            pointer -= a
        else:
            signs.append(0)

    signs.reverse()
    return signs

def Subset_Sum_Plus_Minus_One_Find(A, K):
    """ 以下を満たす A の分割 X, Y の個数を求める: sum(X) - sum(Y) = K.

    計算量: O(|A|(sum(A)+K))
    """

    p = [1 if a >= 0 else -1 for a in A]
    B = list(map(abs, A))

    L = K + sum(B)
    if (L < 0) or (L % 2 == 1):
        return None

    signs = Subset_Sum_Zero_One_Find(B, L // 2)
    if signs is not None:
        return [p[i] * (2 * s - 1) for i, s in enumerate(signs)]
    else:
        return None
