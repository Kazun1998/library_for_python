from Weighted_Digraph import *

def Dijkstra(D: Weigthed_Digraph, start, goal, default = None):
    from heapq import heappush, heappop

    inf = float('inf')
    dist = [inf] * D.order(); dist[start] = 0
    fix = [False] * D.order()
    parent = [None] * D.order()
    upper = [None] * D.order()

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
