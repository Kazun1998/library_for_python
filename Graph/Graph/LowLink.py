from Graph import *

def Lowlink(G: Graph):
    """ G の ord, lowlink を求める.

    G: Graph
    """

    N = G.order()
    tower = []
    children = [[] for _ in range(N)]
    ord = [-1] * N
    low = [-1] * N
    def dfs(start, t):
        ord[start] = low[start] = t
        t += 1
        tower.append(start)
        stack = [(start, v, j) for v, j in G.partner_with_label_yield(start)]
        while stack:
            u, v, j = stack.pop()
            if ord[v] != -1:
                low[u] = min(low[u], ord[v])
                continue

            ord[v] = low[v] = t
            tower.append(v)
            children[u].append(v)
            t += 1
            stack.extend([(v, w, k) for w, k in G.partner_with_label_yield(v) if k != j])
        return t

    t = 0
    for x in range(G.order()):
        if ord[x] == -1:
            t = dfs(x, t)

    for x in reversed(tower):
        for y in children[x]:
            low[x] = min(low[x], low[y])

    return { 'ord': ord, 'low': low }

# 橋列挙
def Bridge(G: Graph):
    """ G にある橋の id を列挙する.

    G: Graph
    """

    data = Lowlink(G)
    ord = data['ord']; low = data['low']
    return [t for u, v, t in G.edge_yielder_with_label() if (ord[u] < low[v]) or (ord[v] < low[u])]

# 関節点の列挙
def Articulation_Point(G):
    from collections import deque

    N=G.vertex_count()
    A=[]; A_append=A.append
    ord=[-1]*N; low=[-1]*N
    flag=[0]*N
    adj=G.adjacent

    parent=[-1]*N; children=[[] for _ in range(N)]

    #BFSパート
    for v in range(N):
        if flag[v]:
            continue

        k=0
        S=deque([v])
        T=[]
        X=[]

        while S:
            u=S.pop()
            if flag[u]:
                continue

            T.append(u)
            ord[u]=k
            k+=1
            flag[u]=1

            for w in adj[u]:
                if not flag[w]:
                    S.append(w)
                    parent[w]=u

        for w in T:
            low[w]=ord[w]

        for w in T[:0:-1]:
            children[parent[w]].append(w)

        for w in T[:0:-1]:
            for x in adj[w]:
                if w==v or x!=parent[w]:
                    low[w]=min(low[w],low[x],ord[x])

        #根での判定
        if len(children[v])>=2:
            A_append(v)

        #根以外の判定
        for w in T[:0:-1]:
            for u in children[w]:
                if ord[w]<=low[u]:
                    A_append(w)
                    break
    return A

#二辺連結成分分解
def Two_Edge_Connected_Components(G: Graph):
    """グラフ G を二辺連結成分分解 (橋を含まない) する.

    [input]
    G: Graph
    """

    bridge = [False] * (G.edge_offset + G.size())
    for j in Bridge(G):
        bridge[j] = True

    comps = []
    t = 0
    comp_id = [-1] * G.order()
    for x in range(G.order()):
        if comp_id[x] != -1:
            continue

        comp_id[x] = t
        c = [x]
        stack = [x]
        while stack:
            u = stack.pop()
            for v, j in G.partner_with_index_yield(u):
                if (not bridge[j]) and (comp_id[v] == -1):
                    comp_id[v] = t
                    c.append(v)
                    stack.append(v)
        comps.append(c)
        t += 1

    return { 'comp_id': comp_id, 'comps': comps }
