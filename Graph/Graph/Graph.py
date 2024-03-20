class Graph:
    __slots__ = ("adjacent", "deg", "__size")

    #入力定義
    def __init__(self, N = 0):
        """ N 頂点の空グラフ (多重辺なし) を生成する."""

        self.adjacent = [[] for _ in range(N)]
        self.deg = [0] * N
        self.__size = 0

    #頂点の追加
    def add_vertex(self):
        """ 頂点を追加する.

        """

        self.adjacent.append([])
        self.deg.append(0)

        return self.order() - 1

    def add_vertices(self, k):
        """ 頂点を k 個追加する.

        k: int
        """

        n = self.order()

        self.adjacent.extend([[] for _ in range(k)])
        self.deg.extend([0] * k)

        return list(range(n, n + k))

    #辺の追加
    def add_edge(self, u, v, label = None):
        """ 無向辺 uv を加える"""

        self.adjacent[u].append((v, label))
        if u != v:
            self.adjacent[v].append((u, label))

        self.deg[u] += 1
        self.deg[v] += 1
        self.__size += 1

    #Walkの追加
    def add_walk(self, *walk):
        """ walk=(w[0],...,w[n-1]) に対して, n-1 本の辺 w[i]w[i+1] を加える."""
        for i in range(len(walk) - 1):
            self.add_edge(walk[i], walk[i + 1])

    #Cycleの追加
    def add_cycle(self, *cycle):
        """ cycle=(c[0], ..., c[n-1]) を加える. """
        self.add_walk(*cycle)
        self.add_edge(cycle[-1], cycle[0])

    def partner_yield(self, v):
        for w, _ in self.adjacent[v]:
            yield w

    def partner(self, v):
        return [w for w, _ in self.adjacent[v]]

    def partner_with_label_yield(self, v):
        yield from self.adjacent[v]

    #近傍
    def neighborhood(self, v):
        """ 頂点 v の近傍を求める. """
        return set(self.partner_yield(v))

    #次数
    def degree(self, v):
        """ 頂点 v の次数を求める. """
        return self.deg[v]

    #頂点数
    def vertex_count(self):
        """ グラフの頂点数 (位数) を出力する. """
        return len(self.adjacent)

    def order(self):
        """ グラフの位数 (頂点数) を出力する. """
        return len(self.adjacent)

    #辺数
    def edge_count(self):
        """ 辺の本数 (サイズ) を出力する."""

        return self.__size

    def size(self):
        """ サイズ (辺の本数) を出力する. """

        return self.__size

    #頂点vを含む連結成分
    def connected_component(self, v):
        """ 頂点 v を含む連結成分を出力する."""

        N = self.order()

        stack = [v]
        comp = [0] * N; comp[v] = 1
        while stack:
            x = stack.pop()
            for y in self.partner_yield(x):
                if comp[y] == 0:
                    comp[y] = 1
                    stack.append(y)

        return [x for x in range(N) if comp[x]]

    #距離
    def distance(self, u, v, default = -1):
        """ 2頂点 u,v 間の距離を求める."""

        if u == v:
            return 0

        from collections import deque

        N = self.order()
        dist = [-1] * N; dist[u]=0

        queue = deque([u])
        while queue:
            x = queue.popleft()
            for y in self.partner_yield(x):
                if dist[y] == -1:
                    dist[y] = dist[x] + 1
                    queue.append(y)

                    if y == v:
                        return dist[v]

        return default

    #ある1点からの距離
    def distance_all(self, u, default = -1):
        """ 頂点 u からの距離を求める."""

        from collections import deque

        N = self.order()
        dist = [-1] * N; dist[u]=0

        queue = deque([u])
        while queue:
            x = queue.popleft()
            for y in self.partner_yield(x):
                if dist[y] == -1:
                    dist[y] = dist[x] + 1
                    queue.append(y)

        return [dist[x] if dist[x] != -1 else default for x in range(N)]

    #最短路
    def shortest_path(self, u, v):
        """ u から v への最短路を求める (存在しない場合は None). """

        if u == v:
            return [u]

        from collections import deque

        prev = [-1] * self.order()
        prev[u] = u

        queue = deque([u])
        while queue:
            x = queue.popleft()
            for y in self.partner_yield(x):
                if prev[y] != -1:
                    continue

                prev[y] = x
                queue.append(y)

                if y != v:
                    continue

                path = [v]
                a = v
                while a != u:
                    a = prev[a]
                    path.append(a)
                return path[::-1]
        return None

    def edge_yielder(self):
        for u in range(self.order()):
            for v in self.partner_yield(u):
                if u <= v:
                    yield (u, v)

    def edge_yielder_with_label(self):
        for u in range(self.order()):
            for v, label in self.partner_with_label_yield(u):
                if u <= v:
                    yield (u, v, label)

#==========
#グラフの生成
#==========
#補グラフの作成
def Complement_Graph(G):
    """ グラフ G の補グラフを求める."""
    pass

# N 頂点のランダムグラフ
def Random_Graph(N, p=0.5, self_loop=False, seed=None):
    pass

def Directed_Sum(*Graphs):
    total_order = sum(G.order() for G in Graphs)
    order_offset = 0

    H = Graph(total_order)
    for G in Graphs:
        for u, v, t in G.edge_yielder():
            H.add_edge(u + order_offset, v + order_offset, t)
        order_offset += G.order()

    return H

#==========
#連結グラフ?
def Is_Connected(G: Graph):
    """ G は連結グラフ ?

    Args:
        G (Graph)
    """

    return (G.order() == 0) or all(d >= 0 for d in G.distance_all(0))

#=====
#森?
def Is_Forest(G: Graph):
    """ 森かどうか判定する. """

    return G.order() == G.size() + Connected_Component_Number(G)

#木?
def Is_Tree(G: Graph):
    """ 木かどうか判定する. """
    return (G.size() == G.order() - 1) and Is_Connected(G)

#木の直径
def Tree_Diameter(T: Graph, Mode = False):
    """ 木 T の直径を求める.

    T: 木

    (出力の結果)
    Mode=True → (直径, (直径を成す端点1, 直径を成す端点2))
    Mode=False → 直径
    """

    def bfs(x):
        dist = [-1] * T.order(); dist[x] = 0
        stack = [x]
        while stack:
            u = stack.pop()

            for v in T.neighborhood(u):
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    stack.append(v)

        y = max(range(T.order()), key = lambda x: dist[x])
        return y, dist[y]

    u, _ = bfs(0)
    v, d = bfs(u)

    if Mode:
        return (d, (u, v))
    else:
        return d

#連結成分に分解
def Connected_Component_Decomposition(G: Graph):
    """ 連結成分毎に分解する.

    G: Graph
    """


    group = [-1] * G.order()
    comps = []

    def dfs(start, g):
        stack = [start]
        group[start] = g
        comp = []

        while stack:
            x = stack.pop()
            comp.append(x)
            for y in G.partner_yield(x):
                if group[y] == -1:
                    group[y] = g
                    stack.append(y)
        comps.append(comp)

    g = 0
    for x in range(G.order()):
        if group[x] == -1:
            dfs(x, g)
            g += 1

    return { 'components': comps, 'group': group }

#連結成分の個数
def Connected_Component_Number(G: Graph):
    """ 連結成分の個数を求める. """

    seen = [False] * G.order()

    def bfs(start):
        seen[start] = True
        stack = [start]

        while stack:
            x = stack.pop()
            for y in G.neighborhood(x):
                if not seen[y]:
                    seen[y] = True
                    stack.append(y)

    count = 0
    for x in range(G.order()):
        if not seen[x]:
            count += 1
            bfs(x)

    return count

#2部グラフ?
def Is_Bipartite_Graph(G: Graph):
    """ 2部グラフかどうかを判定する. """

    seen = [0] * G.order()

    for v in range(G.order()):
        if seen[v] != 0:
            continue

        seen[v] = 1
        stack = [v]
        while stack:
            x = stack.pop()
            for y in G.neighborhood(x):
                if seen[y]==0:
                    seen[y] = -seen[x]
                    stack.append(y)
                elif seen[y] == seen[x]:
                    return False
    return True

#2部グラフの部集合に分割
def Bipartite_Separate(G: Graph):
    """ 2部グラフの頂点を部集合に分割する. """

    N = G.order()
    color = [0] * N

    separates = []
    for v in range(N):
        if color[v] != 0:
            continue

        color[v] = 1
        S = [v]
        A = []; B = []
        while S:
            u = S.pop()

            if color[u]==1:
                A.append(u)
            else:
                B.append(u)

            for w in G.partner_yield(u):
                if color[w] == 0:
                    color[w] = -color[u]
                    S.append(w)
                elif color[w] == color[u]:
                    return None
        separates.append((A,B))

    return separates

#オイラーグラフ?
def Is_Eulerian_Graph(G: Graph):
    """ グラフ G がオイラーグラフかどうかを判定する. """
    return all(G.degree(v) % 2 == 0 for v in range(G.order())) and Is_Connected(G)

#準オイラーグラフ?
def Is_Semi_Eulerian_Graph(G: Graph):
    """ グラフ G が準オイラーグラフかどうかを判定する. """
    return len([v for v in range(G.order()) if G.degree(v) % 2 == 0]) == 2 and Is_Connected(G)

#Euler 路を見つける
def Find_Eulerian_Trail(G):
    pass


#Euler閉路を見つける
def Find_Eulerian_Cycle(G):
    pass

#ハミルトングラフ?
def Is_Hamiltonian_Graph(G):
    """ ハミルトングラフ (全ての頂点を1回ずつ通るサイクルを含むグラフ) かどうかを判定する.

    """
    pass

#ハミルトンを探す.
def Find_Hamiltonian_Graph(G):
    pass

#クリーク
def Clique(G: Graph, calc, merge, unit, empty=False):
    """
    グラフ G に対する Clique C 全てに対する calc (C) を計算し, merge でマージする.

    G: Graph
    calc: calc(C) Clique である部分集合 C に対する値
    merge: merge(x,y) x,y のマージの方法
    empty: 空集合を Clique とするか?

    計算量: O(2^{sqrt(2M)} N)
    """

    N=G.order(); M=G.size()
    deg=[G.degree(v) for v in range(N)]; V=[1]*N

    M_sqrt=0
    while (M_sqrt+1)**2<=2*M:
        M_sqrt+=1

    F = [[False] * N for _ in range(N)]
    for u, v in G.edge_yielder():
        F[u][v] = F[v][u] = True

    X=unit
    while True:
        A=[]
        for u in range(N):
            if V[u] and deg[u]<M_sqrt:
                for v in range(N):
                    if u!=v and V[v] and F[u][v]:
                        A.append(v)
                A.append(u)
                break

        if not A:
            break

        K=len(A)-1
        bit=[0]*K
        for i in range(K):
            for j in range(i):
                if not F[A[i]][A[j]]:
                    bit[i]|=1<<j
                    bit[j]|=1<<i

        for S in range(1<<K):
            flag=1
            for i in range(K):
                if (S>>i)&1:
                    flag&=(S&bit[i]==0)

            if flag:
                B=[A[-1]]
                for i in range(K):
                    if (S>>i)&1:
                        B.append(A[i])

                X=merge(X,calc(B))

        V[A[-1]]=0; deg[A[-1]]=0
        for v in range(N):
            if A[-1]!=v and V[v] and F[A[-1]][v]:
                deg[v]-=1

    A=[]
    for u in range(N):
        if V[u]:
            A.append(u)

    K=len(A)
    bit=[0]*K
    for i in range(K):
        for j in range(i):
            if not F[A[i]][A[j]]:
                bit[i]|=1<<j
                bit[j]|=1<<i

    for S in range(1<<K):
        flag=1
        for i in range(K):
            if (S>>i)&1:
                flag&=(S&bit[i]==0)

        if flag and (S or empty):
            B=[]
            for i in range(K):
                if (S>>i)&1:
                    B.append(A[i])

            X=merge(X,calc(B))

    return X

# 三角形
def Triangle(G: Graph , calc, merge, unit):
    """
    calc: calc(i,j,k) 3頂点 i,j,k からなる頂点に対する値
    merge: merge(x,y) x,y のマージの方法
    unit: 単位元

    計算量: O(M sqrt(2M))
    """

    N=G.order()
    A=[[] for _ in range(N)]

    deg=G.degree
    for i in range(N):
        for j in G.neighborhood(i):
            if (deg(i)>deg(j)) or (deg(i)==deg(j) and i>j):
                A[i].append(j)

    X=unit
    used=[False]*N
    for i in range(N):
        for k in A[i]:
            used[k]=True

        for j in A[i]:
            for k in A[j]:
                if used[k]:
                    X=merge(X,calc(i,j,k))
        for k in A[i]:
            used[k]=False
    return X

#=================================================
#特別なグラフ
#=================================================
#完全グラフの作成
def Complete_Graph(N):
    """ N 頂点の完全グラフを生成する. """

    G=Graph(N)
    for u in range(N):
        for v in range(u+1,N):
            G.add_edge(u,v)
    return G

#完全2部グラフ
def Complete_Bipartite_Graph(M,N):
    """ M,N 頂点の完全2部グラフを生成する. """

    G=Graph(M+N)

    for a in range(M):
        for b in range(M,M+N):
            G.add_edge(a,b)
    return G

#グラフ作成
def Making_Graph(N,E):
    """ 辺の情報 E からグラフを生成する. """

    G=Graph(N)
    for e in E:
        G.add_edge(*e)
    return G

#ペテルセングラフ
def Petersen_Graph(N=5,K=2):
    """ (n,k) -型のペテルセングラフを紹介する. """

    G=Graph(2*N)

    for i in range(N):
        G.add_edge(i,(i+1)%N)
        G.add_edge(i,i+N)

        j=(i+K)%N
        G.add_edge(i+N,j+N)
    return G

#格子グラフ
def Grid_Graph(M, N):
    """ M x N マスのグラフを生成する.  """

    G=Graph(M*N)

    for p in range(M*N):
        if p%N!=N-1:
            G.add_edge(p,p+1)
        if p<(M-1)*N:
            G.add_edge(p,p+N)
    return G

#トーラス
def Torus_Graph(M, N):
    """ M x N のトーラスグラフを生成する. """

    G=Graph(M*N)
    for i in range(M):
        for j in range(N):
            p=i*N+j
            q=i*N+(j+1)%N
            r=((i+1)%M)*N+j

            G.add_edge(p,q)
            G.add_edge(p,r)
    return G

#Pathグラフ
def Path_Graph(N):
    """ N 頂点からなるパスグラフを生成する. """

    P=Graph(N)
    for i in range(N-1):
        P.add_edge(i,i+1)
    return P

#Cycleグラフ
def Cycle_Graph(N):
    """ N 頂点からなるサイクルグラフを生成する. """

    C=Graph(N)
    for i in range(N):
        C.add_edge(i, (i+1)%N)
    return C

#Circulant グラフ
def Circulant_Graph(N, *J):
    """ N 頂点, J ジャンプの巡回グラフを生成する."""

    C=Graph(N)
    for j in J:
        for v in range(N):
            w=(v+j)%N
            C.add_edge(v,w)
    return C

#Starグラフ
def Star_Graph(N):
    """ 葉を N 個持つスターグラフを生成する. """

    S=Graph(N+1)
    for i in range(1,N+1):
        S.add_edge(0,i)
    return S

#Wheelグラフ
def Wheel_Graph(N):
    """ 外周部が N 頂点からなる車輪グラフを生成する. """

    W=Graph(N+1)
    for i in range(1,N+1):
        W.add_edge(0,i)

    for j in range(N):
        W.add_edge(j%N+1,(j+1)%N+1)
    return W

#騎士巡回グラフ
def Knight_Tour_Graph(M, N, s=1, t=2):
    """ M x N のチェス盤に (s,t)-Knight が移動するグラフを生成する.
    """

    G=Graph(M*N)

    H=[(s,t),(t,s),(s,-t),(t,-s)]

    for a,b in H:
        for i in range(max(0,-a),min(M,M-a)):
            for j in range(max(0,-b),min(N,N-b)):
                p=i*N+j; q=(i+a)*N+(j+b)
                G.add_edge(p,q)
    return G

#完全k分木
def Complete_Kary_Tree(n,k=2):
    """ 深さが n の完全 k 分木を生成する. """

    m=(k**n-1)//(k-1)
    T=Graph(m)

    for i in range(1,m):
        T.add_edge((i-1)//k,i)
    return T

#==========
# グラフの走査
#==========
def Depth_First_Search_yielder(G):
    """ 深さ優先探索を行う.

    [Input]
    G: グラフ

    [Output]
    (-1, v, 1): v が探索開始の頂点である.
    (u,v,1): u から v へ向かう辺で, DFS 木で葉に進む向きになる辺
    (u,v,0): u から v へ向かう辺で後退辺 (DFS 木には不採用)
    (u,v,-1): u から v へ向かう辺で, DFS 木では根に進む向きになる辺
    (u,-1,-1): u から始まった DFS が終了
    """

    from collections import deque

    N=G.vertex_count(); adj=[list(a) for a in G.adjacent]
    T=[0]*N; R=[0]*N; parent=[-1]*N

    for x in range(N):
        if T[x]==0:
            S=deque([x])

            yield (-1, x, 1)
            while S:
                x=S.pop()
                T[x]=1

                while R[x]<len(adj[x]):
                    y=adj[x][R[x]]
                    R[x]+=1

                    if T[y]==0:
                        S.append(x); S.append(y)
                        parent[y]=x
                        yield (x,y,1)
                        break
                    else:
                        yield (x,y,0)
                else:
                    yield (x, parent[x], -1)
            yield (x, -1, -1)
