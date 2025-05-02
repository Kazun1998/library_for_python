from Graph import Graph

def Complete_Graph(N: int) -> Graph:
    """ N 頂点の完全グラフ K_n を生成する

    Args:
        N (int): 位数

    Returns:
        Graph: N 頂点の完全グラフ K_n
    """

    G = Graph(N)
    for u in range(N):
        for v in range(u + 1, N):
            G.add_edge(u, v)
    return G

def Cycle(N: int) -> Graph:
    """ N 頂点のサイクルグラフを作成する.

    Args:
        N (int): 位数

    Returns:
        Graph: N 頂点のサイクル C_N
    """

    C = Graph(N)
    for i in range(N):
        C.add_edge(i, (i + 1) % N)
    return C

def Complete_Bipartite_Graph(M: int, N: int) -> Graph:
    """ M 頂点と N 頂点の完全二部グラフ K_{M,N} を生成する.

    Args:
        M (int): 位数 (1)
        N (int): 位数 (2)

    Returns:
        Graph: 完全二部グラフ K_{M,N}
    """
    G = Graph(M + N)

    for a in range(M):
        for b in range(M, M + N):
            G.add_edge(a, b)
    return G

def Petersen_Graph(n: int= 5, k: int= 2) -> Graph:
    """ (n, k) 型のペテルセングラフを生成する

    Args:
        n (int, optional): Defaults to 5.
        k (int, optional): Defaults to 2.

    Returns:
        Graph: (n, k) 型のペテルセングラフ
    """

    G = Graph(2 * n)

    for i in range(n):
        G.add_edge(i, (i + 1) % n)
        G.add_edge(i, i + n)

        j = (i + k) % n
        G.add_edge(i + n, j + n)
    return G

def Grid_Graph(M: int, N: int) -> Graph:
    """ 縦 M 頂点, 横 N 頂点の格子グラフを生成する.

    Args:
        M (int): 縦の頂点数
        N (int): 横の頂点数

    Returns:
        Graph: 縦 M 頂点, 横 N 頂点の格子グラフ
    """

    G = Graph(M * N)

    for i in range(M):
        for j in range(N):
            # 縦
            if i < M - 1:
                G.add_edge(i * N + j, (i + 1) * N + j)

            # 横
            if j < N - 1:
                G.add_edge(i * N + j, i * N + j + 1)

    return G

def Torus_Graph(M: int, N: int) -> Graph:
    """ 縦 M 頂点, 横 N 頂点のトーラスグラフを生成する.

    Args:
        M (int): 縦の頂点数
        N (int): 横の頂点数

    Returns:
        Graph: 縦 M 頂点, 横 N 頂点のトーラスグラフ
    """

    G = Graph(M * N)
    for i in range(M):
        for j in range(N):
            p = i * N + j
            q = i * N + (j + 1) % N
            r = ((i + 1) % M) * N + j

            G.add_edge(p, q)
            G.add_edge(p, r)
    return G

def Path_Graph(N: int) -> Graph:
    """ N 頂点のパスグラフを生成する.

    Args:
        N (int): 位数

    Returns:
        Graph: N 頂点のパスグラフ
    """

    P = Graph(N)
    for i in range(N - 1):
        P.add_edge(i, i + 1)
    return P

def Star_Graph(N: int) -> Graph:
    """ N 個の葉を持つスターグラフを生成する.

    Args:
        N (int): 葉の数

    Returns:
        Graph: N 個の葉を持つスターグラフ
    """

    S = Graph(N + 1)
    for i in range(1, N + 1):
        S.add_edge(0, i)
    return S

def Wheel_Graph(N: int) -> Graph:
    """ 外周部が N 個の頂点からなる車輪グラフを生成する.

    Args:
        N (int): 外周部の頂点数

    Returns:
        Graph: 外周部が N 個の頂点からなる車輪グラフ
    """


    W = Graph(N + 1)
    for i in range(1, N + 1):
        W.add_edge(0, i)

    for j in range(N):
        W.add_edge(j % N + 1, (j + 1) % N + 1)
    return W

def Circulant_Graph(N: int, *J: tuple[int]) -> int:
    """ N 頂点, J ジャンプの巡回グラフを生成する."""

    C = Graph(N)
    for j in J:
        for v in range(N):
            w = (v + j) % N
            C.add_edge(v, w)
    return C

def Knight_Tour_Graph(M: int, N: int, s: int = 1, t: int = 2) -> Graph:
    """ M x N のチェス盤に (s,t) Knight が移動するグラフを生成する.

    Args:
        M (int): チェス盤の縦のマスの数
        N (int): チェス盤の横のマスの数
        s (int, optional): 騎士のパラメータ (1). Defaults to 1.
        t (int, optional): 騎士のパラメータ (2). Defaults to 2.

    Returns:
        Graph: M x N のチェス盤に (s,t) Knight が移動するグラフ
    """
    G = Graph(M * N)

    for di, dj in [(s, t), (t, s), (s, -t), (t, -s)]:
        for i in range(max(0, -di), min(M, M - di)):
            for j in range(max(0, -dj), min(N, N - dj)):
                p = i * N + j
                q = (i + di) * N + (j + dj)
                G.add_edge(p, q)
    return G

def Complete_Kary_Tree(n: int, k=2) -> Graph:
    """ 深さ n の完全 k 部グラフを生成する.

    Args:
        n (int): 深さ
        k (int, optional): 子の数. Defaults to 2.

    Returns:
        Graph: 深さ n の完全 k 部グラフ
    """

    m = (pow(k, n) - 1) // (k - 1)
    T = Graph(m)

    for i in range(1, m):
        T.add_edge((i - 1) // k, i)

    return T