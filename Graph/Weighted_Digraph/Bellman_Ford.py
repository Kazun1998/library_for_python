from Weighted_Digraph import *

def Bellman_Fold(D: Weigthed_Digraph, start, goal, default = None):
    N = D.order()

    arcs = []
    for u in range(N):
        arcs.extend([(u, v, w) for v, w, _ in D.adjacent_out[u]])

    inf = float('inf')
    dist = [inf] * N; dist[start] = 0

    for _ in range(N - 1):
        updated = False
        for u, v, w in arcs:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True

        if not updated:
            break

    # 負閉路検出
    for _ in range(N):
        updated = False
        for u, v, w in arcs:
            if dist[u] + w < dist[v]:
                dist[v] = -inf
                updated = True

        if not updated:
            break

    return dist[goal]
