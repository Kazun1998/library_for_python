from Weighted_Digraph import *

def Dijkstra(D: Weigthed_Digraph, start: int, goal: int, default = None) -> dict:
    """ 重み付き有向グラフ D において, start から goal までの最短路を Dijkstra 法によって求める.

    Args:
        D (Weigthed_Digraph): 重み付き有向グラフ
        start (int): 始点
        goal (int): 終点
        default (optional): start から goal までの歩道が存在しない場合の距離の帰り値. Defaults to None.

    Returns:
        dict:
            dist: 最短路の長さ
            arc: 最短路をなす弧の番号
            vertex: 最短路をなす頂点の番号
    """

    from heapq import heappush, heappop

    inf = D.infinity
    dist = D.initialize_list(inf); dist[start] = 0
    fix = D.initialize_list(False)
    parent = D.initialize_list(None)
    upper = D.initialize_list(None)

    Q = [(0, start)]
    while Q:
        d, x = heappop(Q)
        if fix[x]:
            continue

        fix[x] = True
        if x == goal:
            break

        for y, w, id in D.adjacent_out[x]:
            if d + w < dist[y]:
                dist[y] = d + w
                parent[y] = x
                upper[y] = id
                heappush(Q, (dist[y], y))

    if dist[goal] == inf:
        return {'dist': default, 'arc': None, 'vertex': None}

    vertex = [goal]
    arc = []
    x = goal
    while x != start:
        arc.append(upper[x])
        x = parent[x]
        vertex.append(x)

    return {'dist': dist[goal], 'arc': arc[::-1], 'vertex': vertex[::-1]}

def Dijkstra_All(D: Weigthed_Digraph, start: int, default = None) -> dict:
    """ 重み付き有向グラフ D について, start を始点とする距離を各頂点について求める.

    Args:
        D (Weigthed_Digraph): 重み付き有向グラフ (全ての辺の重みが正であることを要求する)
        start (int): 始点
        default (optional): 到達不能の場合の返り値. Defaults to None.

    Returns:
        dict
    """

    from heapq import heappop, heappush

    N = D.order
    dist = D.initialize_list(D.inifinity)
    dist[start] = 0

    prev = D.initialize_list(None)
    prev[start] = start

    Q = [(0, start)]
    while Q:
        d, x = heappop(Q)

        if d > dist[x]:
            continue

        for y, w, _ in D.adjacent_out[x]:
            if d + w < dist[y]:
                dist[y] = d + w
                heappush(Q, (dist[y], y))
                prev[y] = x

    return { 'dist': [dist[x] if dist[x] < D.infinity else default for x in range(N)], 'prev': prev }
