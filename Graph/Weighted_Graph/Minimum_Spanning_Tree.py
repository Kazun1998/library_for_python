from Weighted_Graph import Weigthed_Graph

# 最小全域木をクラシカル法で求める.
def Minimum_Spanning_Tree_by_Kruskal(G: Weigthed_Graph):
    """ グラフ G の最小全域木をクラシカル法で求める.

    G: グラフ
    """

    N = G.order()

    #Union-Findを定義する.
    UF = list(range(N))
    depth = [0] * N

    def find(x):
        y = x
        while UF[y] != y:
            y = UF[y]

        while UF[x] != y:
            x, UF[x] = UF[x], y

        return y

    def union(x, y):
        x = find(x)
        y = find(y)

        if x == y:
            return False

        if depth[x] > depth[y]:
            UF[y] = x
        else:
            UF[x] = y
            if depth[x] == depth[y]:
                depth[y] += 1
        return True

    k = G.edge_offset + G.size()

    u = [0] * k
    v = [0] * k
    w = [0] * k
    for x, y, z, id in G.edge_yielder():
        u[id] = x
        v[id] = y
        w[id] = z

    edges = []
    remain = N - 1

    for id in sorted(range(G.edge_offset, k), key = lambda id: w[id]):
        if not union(u[id], v[id]):
            continue

        edges.append(id)
        remain -= 1

        if remain == 0:
            continue

    return { 'weight': sum(w[id] for id in edges), 'edges': edges }

# 最小全域木をプリム法で求める.
def Minimum_Spanning_Tree_by_Prim(G: Weigthed_Graph):
    """ グラフ G の最小全域木をプリム法で求める.
    """
    from heapq import heapify, heappop, heappush
    N = G.vertex_count()

    used = [0] * N; used[0] = 1
    Q = [(w, 0, y, id) for y, w, id in G.adjacent[0]]
    heapify(Q)

    weight = 0
    remain = N - 1
    edges = []

    while remain:
        c, _, b, id = heappop(Q)

        if used[b]:
            continue

        remain -= 1
        weight += c
        edges.append(id)

        used[b] = 1
        for v, w, id in G.adjacent[b]:
            if not used[v]:
                heappush(Q, (w, b, v, id))

    return { 'weight': weight, 'edges': edges }
