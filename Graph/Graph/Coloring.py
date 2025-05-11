from Graph import *

def Chromatic_Number(G: Graph) -> int:
    """ 自己ループを持たない無向グラフ G の彩色数を求める.

    Args:
        G (Graph): 自己ループを持たない無向グラフ

    Returns:
        int: 彩色数
    """

    N = G.order

    def zeta(X: list[int]) -> list[int]:
        Y = X.copy()
        for x in range(N):
            b = (1 << x)
            for S in range(1 << N):
                if bit(S, x):
                    Y[S] += Y[S ^ b]
        return Y

    def mebious(Y: list[int]) -> list[int]:
        X = Y.copy()
        for x in range(N):
            b = 1<< x
            for S in range(1<<N):
                if bit(S, x):
                    X[S] -= X[S ^ b]
        return X

    def autocorrelation(A: list[int]) -> list[int]:
        A_zeta = zeta(A)
        return mebious([a * a for a in A_zeta])

    def convolution(A: list[int], B: list[int]) -> list[int]:
        return mebious([a * b for a, b in zip(zeta(A), zeta(B))])

    def lowest_bit(x: int) -> int:
        return (x & (-x)).bit_length() - 1

    bit = lambda x, k: (x >> k) & 1

    def bits(x: int) -> list[int]:
        return [k for k in range(N) if bit(x, k)]

    edge_table = [[False] * N for _ in range(N)]
    for edge in G.edge_generator():
        u = edge.source
        v = edge.target
        edge_table[u][v] = edge_table[v][u] = True

    # 方針: dp[k][S] := 誘導グラフ G[S] は k 色で彩色可能 ?

    # Section I: dp[1][S] を求める. (iff S は独立集合?)
    dp_1 = [0] * (1 << N)
    dp_1[0] = 1
    for S in range(1, 1 << N):
        x = lowest_bit(S)
        if not dp_1[S ^ (1 << x)]:
            continue

        dp_1[S] = int(not any(edge_table[x][y] for y in bits(S ^ (1 << x))))

    # 空グラフの彩色数は 1
    if dp_1[-1]:
        return 1

    dp = { 1: dp_1 }

    # Section II: k = 2, 4, 8, ..., に対して, dp_k[V] が True になるかどうかを判定する.
    while True:
        k = max(dp)
        if 2 * k > N:
            break

        conv = autocorrelation(dp[k])
        dp[2 * k] = [1 if x else 0 for x in conv]
        if dp[2 * k][-1]:
            break

    # Section III: 二分探索によって彩色数を求める
    prev = dp[k]
    step = k >> 1
    while step:
        if k + step > N:
            step >>= 1
            continue

        res = [1 if x else 0 for x in convolution(prev, dp[step])]
        dp[k + step] = res
        if not res[-1]:
            k += step
            prev = res

        step >>= 1

    return k + 1

def Clique_Cover_Number(G: Graph):
    """ G をクリークで分割するために必要なクリークの数の最小値を求める.
    この値は G の補グラフの彩色数と一致する.

    Args:
        G (Graph): 無向グラフ

    Returns:
        int
    """
    return Clique_Cover_Number(Complement_Graph(G))