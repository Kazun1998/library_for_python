from Weighted_Graph import *

def Dijkstra(G: Weigthed_Graph, start: int, goal: int, default = None):
    from heapq import heappop, heappush

    inf = float('inf')
    N = G.vertex_count()
    dist = [inf] * N; dist[start] = 0
    fix = [False] * N
    upper = [None] * N
    parent = [None] * N

    Q = [(0, start)]
    while Q:
        d, x = heappop(Q)

        if fix[x]:
            continue

        if x == goal:
            break

        for y, w, id in G.adjacent[x]:
            if not (d + w < dist[y]):
                continue

            dist[y] = d + w
            parent[y] = x
            upper[y] = id
            heappush(Q, (dist[y], y))

    if dist[goal] == inf:
        return {'dist': default, 'arc': None, 'vertex': None}

    vertex = [goal]
    edge = []
    x = goal
    while x != start:
        edge.append(upper[x])
        x = parent[x]
        vertex.append(x)

    return {'dist': dist[goal], 'arc': edge[::-1], 'vertex': vertex[::-1]}
