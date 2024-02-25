from Weighted_Digraph import *

def Warshall_Floyd(D: Weigthed_Digraph):
    """ Warshall-Floyd 法を用いて, 全点間距離を求める.

    D: 重み付き有向グラフ
    """

    N = D.order()
    inf = float('inf')

    dist = [[0 if u == v else inf for v in range(N)] for u in range(N)]

    def three_loop():
        for r in range(N):
            dist_r = dist[r]
            for p in range(N):
                dist_p = dist[p]
                for q in range(N):
                    dist_p[q] = min(dist_p[q], dist_p[r] + dist_r[q])

    for u in range(N):
        dist_u = dist[u]
        for v, w, _ in D.adjacent_out[u]:
            dist_u[v] = min(dist_u[v], w)

    three_loop()

    if any(dist[u][u] < 0 for u in range(N)):
        for u in [u for u in range(N) if dist[u][u] < 0]:
            dist[u][u] = -inf
        three_loop()

    return dist