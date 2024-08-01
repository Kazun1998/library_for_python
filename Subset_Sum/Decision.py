def Subset_Sum_Zero_One_Decision(A, S):
    """ A の多重部分集合で, 和が S になる (0, 1) 列の例を求める.

    計算量: O(|A| S)
    """

    DP = [False] * (S + 1); DP[0] = True
    DP_prev = [False] * (S + 1)

    for a in A:
        DP_prev, DP = DP, DP_prev
        for x in range(S + 1):
            DP[x] = DP_prev[x]

        for y in range(S, a - 1, -1):
            DP[y] |= DP_prev[y - a]

    return DP[S]

def Subset_Sum_Plus_Minus_One_Decision(A, K):
    """ 以下を満たす A の分割 X, Y の個数を求める: sum(X) - sum(Y) = K.

    計算量: O(|A|(sum(A)+K))
    """

    B = list(map(abs, A))

    L = K + sum(B)
    return (L >= 0) and (L % 2 == 0) and Subset_Sum_Zero_One_Decision(B, L // 2)
