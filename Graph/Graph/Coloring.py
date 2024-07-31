from Graph import *

def Chromatic_Number(G: Graph):
    N = G.order()

    def zeta(X):
        Y = X.copy()
        for x in range(N):
            b = (1 << x)
            for S in range(1 << N):
                if bit(S, x):
                    Y[S] += Y[S ^ b]
        return Y

    def mebious(Y):
        X = Y.copy()
        for x in range(N):
            b = 1<< x
            for S in range(1<<N):
                if bit(S, x):
                    X[S] -= X[S ^ b]
        return X

    def convolution(A, B):
        return mebious([a * b for a, b in zip(zeta(A), zeta(B))])

    def lowest_bit(x: int):
        return (x & (-x)).bit_length() - 1

    bit = lambda x, k: (x >> k) & 1

    def bits(x):
        return [k for k in range(N) if bit(x, k)]

    edge = [[False] * N for _ in range(N)]
    for u, v in G.edge_yielder():
        edge[u][v] = edge[v][u] = True

    # 方針: dp[k][S] := 誘導グラフ G[S] は k 色で彩色可能 ?

    # Section I: dp[1][S] を求める. (iff S は独立集合?)
    dp = [None];
    dp.append([0] * (1 << N)); dp[1][0] = 1
    dp_1 = dp[1]
    for S in range(1, 1 << N):
        x = lowest_bit(S)
        if not dp_1[S ^ (1 << x)]:
            continue

        dp_1[S] = int(not any(edge[x][y] for y in bits(S ^ (1 << x))))

    # 空グラフの彩色数は 1
    if dp_1[-1]:
        return 1

    # Section II: dp_k[V] が True になる最小の k を求める
    for k in range(2, N + 1):
        dp.append(convolution(dp_1, dp[-1]))
        dp[k] = list(map(lambda x: 1 if x else 0, dp[-1]))

        if dp[k][-1]:
            return k

def Clique_Cover_Number(G: Graph):
    """ G をクリークで分割するために必要なクリークの数の最小値を求める.
    この値は G の補グラフの彩色数と一致する.

    Args:
        G (Graph): 無向グラフ

    Returns:
        int
    """
    return Clique_Cover_Number(Complement_Graph(G))