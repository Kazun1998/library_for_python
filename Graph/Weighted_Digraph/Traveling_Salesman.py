from Weighted_Digraph import *

def Traveling_Salesman(D: Weigthed_Digraph, default = -1):
    """ 巡回セールスマン問題を解く

    Args:
        D (Weigthed_Digraph)
    """

    N = D.order()

    dp = [[default] * N for _ in range(1 << N)]
    dp[0][0] = 0

    bit = lambda S, k: (S >> k) & 1

    for S in range(1 << N):
        dp_S = dp[S]
        for x in range(N):
            if bit(S, x):
                continue

            dp_T = dp[S | (1 << x)]
            for y, w, _ in D.adjacent_in[x]:
                if dp_S[y] == default:
                    continue
                elif dp_T[x] == default:
                    dp_T[x] = dp_S[y] + w
                else:
                    dp_T[x] = min(dp_T[x], dp_S[y] + w)
    return dp[-1][0]
