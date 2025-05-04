from Weighted_Digraph import *

def Bellman_Ford(D: Weighted_Digraph, start: int, goal: int, default: int = None) -> int:
    """ 頂点 start から頂点 goal への最短路の長さを Bellman Ford 法で求める.

    Args:
        D (Weighted_Digraph): 重み付き有向グラフ
        start (int): 始点
        goal (int): 終点
        default (int, optional): 頂点 start から頂点 goal へのパスが存在しない場合の返り値. Defaults to None.

    Returns:
        int: 頂点 start から頂点 goal への最短路の長さ
    """

    inf = D.infinity
    N = D.order

    dist = D.initialize_list(inf)
    dist[start] = 0

    arcs = [(arc.source, arc.target, arc.weight) for arc in D.arcs_generator()]

    def update_dist(negative_cycle: bool) -> bool:
        updated = False
        for source, target, weight in arcs:
            if dist[source] >= inf or not(dist[source] + weight < dist[target]):
                continue

            if negative_cycle:
                dist[target] = -float('inf')
            else:
                dist[target] = dist[source] + weight
            updated = True

        return updated

    for _ in range(N):
        if not update_dist(False):
            return dist[goal] if dist[goal] < inf else default

    for _ in range(N):
        if not update_dist(True):
            break

    return dist[goal] if dist[goal] < inf else default

def Bellman_Ford_All(D: Weighted_Digraph, start: int) -> list[int]:
    """ Bellman-Ford 法を用いて, 各頂点への単一始点 start からの距離を求める (いくらでも小さくできる場合は -inf).

    Args:
        D (Weighted_Digraph): 重み付き有向グラフ
        start (int): 始点

    Returns:
        list[int]: 第 v 要素は頂点 v への start からの距離
    """

    inf = D.inifinity
    N = D.order

    dist = D.initialize_list(inf)
    dist[start] = 0

    edges = []
    for u in range(N):
        for v, weight, _ in D.adjacent_out[u]:
            edges.append((u, v, weight))

    def update_dist(negative_cycle: bool) -> bool:
        updated = False
        for u, v, weight in edges:
            if dist[u] >= inf or not(dist[u] + weight < dist[v]):
                continue

            if negative_cycle:
                dist[v] = -float('inf')
            else:
                dist[v] = dist[u] + weight
            updated = True

        return updated

    for _ in range(N):
        if not update_dist(False):
            return dist

    for _ in range(N):
        if not update_dist(True):
            break

    return dist
