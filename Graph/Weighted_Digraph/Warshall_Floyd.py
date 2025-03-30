from Weighted_Digraph import *

def Warshall_Floyd(D: Weighted_Digraph) -> list[list[int]]:
    """ Warshall-Floyd 法を用いて, 全点間距離を求める.

    Args:
        D (Weighted_Digraph): 無向グラフ

    Returns:
        list[list[int]]: (i, j) 成分が i, j 間の距離. ただし, 負の閉路による影響を受ける場合は -inf
    """

    def three_loop():
        for u, du in enumerate(dist):
            for _, dv in enumerate(dist):
                for w in range(N):
                    dv[w] = min(dv[w], dv[u] + du[w])

    inf = D.inifinity
    N = D.vertex_count

    dist = [[0 if i == j else inf for j in range(N)] for i in range(N)]
    for arc in D.arcs_generator():
        dist[arc.source][arc.target] = min(dist[arc.source][arc.target], arc.weight)

    three_loop()

    if any(dist[v][v] < 0 for v in range(N)):
        for v in range(N):
            if dist[v][v] < 0:
                dist[v][v] = -float('inf')
        three_loop()

    return dist
