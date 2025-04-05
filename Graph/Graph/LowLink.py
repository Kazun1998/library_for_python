from Graph import *

def Lowlink(G: Graph):
    """ G の ord, lowlink を求める.

    G: Graph
    """

    N = G.order
    tower = []
    children = [[] for _ in range(N)]
    ord = [-1] * N
    low = [-1] * N
    def dfs(start, t):
        ord[start] = low[start] = t
        t += 1
        tower.append(start)
        stack = [(start, edge.id) for edge in G.adjacent[start]]
        while stack:
            u, j = stack.pop()
            edge = G.get_edge(j, u)
            v = edge.target
            if ord[v] != -1:
                low[u] = min(low[u], ord[v])
                continue

            ord[v] = low[v] = t
            tower.append(v)
            children[u].append(v)
            t += 1
            stack.extend([(v, e.id) for e in G.adjacent[v] if e.id != j])
        return t

    t = 0
    for x in range(G.order):
        if ord[x] == -1:
            t = dfs(x, t)

    for x in reversed(tower):
        for y in children[x]:
            low[x] = min(low[x], low[y])

    return { 'ord': ord, 'low': low }

# 橋列挙
def Bridge(G: Graph) -> list[Edge]:
    """ G にある橋のリストを求める

    Args:
        G (Graph): グラフ

    Returns:
        list[Edge]: 橋のリスト
    """

    data = Lowlink(G)
    ord = data['ord']
    low = data['low']

    return [edge for edge in G.edge_generator() if (ord[edge.source] < low[edge.target]) or (ord[edge.target] < low[edge.source])]

# 関節点の列挙
def Articulation_Point(G: Graph) -> list[int]:
    from collections import deque

    N = G.vertex_count
    articulations: list[int] = []
    ord = [-1] * N
    low = [-1] * N
    flag = [0] * N

    parent = [-1] * N
    children: list[list[int]] = [[] for _ in range(N)]

    #BFSパート
    for v in range(N):
        if flag[v]:
            continue

        k = 0
        S = deque([v])
        T = []

        while S:
            u = S.pop()
            if flag[u]:
                continue

            T.append(u)
            ord[u] = k
            k += 1
            flag[u] = 1

            for edge in G.adjacent[u]:
                w = edge.target
                if not flag[w]:
                    S.append(w)
                    parent[w] = u

        for w in T:
            low[w] = ord[w]

        for w in T[:0:-1]:
            children[parent[w]].append(w)

        for w in T[:0:-1]:
            for edge in G.adjacent[w]:
                x = edge.target
                if (w == v) or (x != parent[w]):
                    low[w] = min(low[w], low[x], ord[x])

        #根での判定
        if len(children[v]) >= 2:
            articulations.append(v)

        #根以外の判定
        for w in T[:0:-1]:
            for u in children[w]:
                if ord[w] <= low[u]:
                    articulations.append(w)
                    break
    return articulations

# 二辺連結成分分解
def Two_Edge_Connected_Components(G: Graph) -> list[int]:
    """ グラフ G を二辺連結成分分分解する.

    Args:
        G (Graph): グラフ

    Returns:
        list[int]: 二重連結成分分解の頂点からなるリスト
    """

    bridge_ids = set([edge.id for edge in Bridge(G)])

    components = []
    group = [None] * G.order
    for x in range(G.order):
        if group[x] is not None:
            continue

        t = len(components)
        group[x] = t
        component = [x]
        stack = [x]
        while stack:
            u = stack.pop()
            for edge in G.adjacent[u]:
                v = edge.target
                if (edge.id not in bridge_ids) and (group[v] is None):
                    group[v] = t
                    component.append(v)
                    stack.append(v)
        components.append(component)

    return { 'group': group, 'components': components }
