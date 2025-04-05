class Edge:
    def __init__(self, id: int, source: int, target: int):
        self.__id = id
        self.__source = source
        self.__target = target

    def fetch_reversal_edge(self) -> "Edge":
        reversal_edge = Edge(self.id, self.target, self.source)
        self.__reversal = reversal_edge
        reversal_edge.__reversal = self

    @property
    def id(self) -> int:
        return self.__id

    @property
    def source(self) -> int:
        return self.__source

    @property
    def target(self) -> int:
        return self.__target

    @property
    def reversal(self) -> "Edge":
        return self.__reversal

class Graph:
    __slots__ = ("adjacent", "deg", "edges", "__edge_offset")

    #入力定義
    def __init__(self, N = 0, edge_offset: int = 0):
        """ N 頂点の空グラフ (多重辺なし) を生成する."""

        self.adjacent: list[list[Edge]] = [[] for _ in range(N)]
        self.edges: list[Edge] = [None] * edge_offset
        self.deg = [0] * N
        self.__edge_offset = edge_offset

    @classmethod
    def construct_from_edge_edges(cls, N: int, edges: list[tuple[int, int]]) -> "Graph":
        """ 隣接リストから N 頂点の無向グラフを生成する.

        Args:
            N (int): 位数
            adjacent (list[int]): 隣接リスト

        Returns:
            Graph: 隣接リストからなる無向グラフ
        """

        G: Graph = Graph(N)
        for u, v in edges:
            G.add_edge(u, v)
        return G

    # property
    @property
    def vertex_count(self) -> int:
        """ グラフの頂点数 (位数) を出力する.

        Returns:
            int: 頂点数
        """
        return len(self.adjacent)

    @property
    def order(self) -> int:
        """ グラフの位数 (頂点数) を出力する.

        Returns:
            int: 位数
        """
        return len(self.adjacent)

    #辺数
    @property
    def edge_count(self) -> int:
        """ グラフの辺の本数 (サイズ) を出力する.

        Returns:
            int: 辺の本数
        """

        return len(self.edges) - self.__edge_offset

    @property
    def size(self) -> int:
        """ グラフのサイズ (辺の本数) を出力する.

        Returns:
            int: サイズ
        """

        return len(self.edges) - self.__edge_offset

    #頂点の追加
    def add_vertex(self) -> int:
        """ 頂点を 1 個追加する.

        Returns:
            int: 追加された頂点の番号
        """

        self.adjacent.append([])
        self.deg.append(0)

        return self.order - 1

    def add_vertices(self, k: int) -> list[int]:
        """ 頂点を k 個追加する.

        Args:
            k (int): 追加する頂点の数

        Returns:
            list[int]: 追加された k 個の頂点の番号からなるリスト
        """

        n = self.order

        self.adjacent.extend([[] for _ in range(k)])
        self.deg.extend([0] * k)

        return list(range(n, n + k))

    #辺の追加
    def add_edge(self, u: int, v: int) -> "Edge":
        """ 辺 uv を加える

        Args:
            u (int): 頂点
            v (int): 頂点

        Returns:
            Edge: 追加された辺
        """

        id = len(self.edges)
        edge = Edge(id, u, v)
        self.adjacent[u].append(edge)
        if u != v:
            edge.fetch_reversal_edge()
            self.adjacent[v].append(edge.reversal)

        self.deg[u] += 1
        self.deg[v] += 1
        self.edges.append(edge)
        return edge

    #Walkの追加
    def add_walk(self, *walk: int):
        """ walk=(w[0],...,w[n-1]) に対して, n-1 本の辺 w[i]w[i+1] を加える."""
        for i in range(len(walk) - 1):
            self.add_edge(walk[i], walk[i + 1])

    #Cycleの追加
    def add_cycle(self, *cycle: int):
        """ cycle=(c[0], ..., c[n-1]) を加える. """
        self.add_walk(*cycle)
        self.add_edge(cycle[-1], cycle[0])

    #次数
    def degree(self, v: int) -> int:
        """ 頂点 v の次数を求める.

        Args:
            v (int): 頂点

        Returns:
            int: 頂点 v の次数
        """

        return self.deg[v]

    def get_edge(self, edge_id: int, source: int = None) -> Edge:
        """ id が edge_id である辺を取得する.

        Args:
            edge_id (int): 取得する edge の番号

        Returns:
            Edge: edge
        """

        edge = self.edges[edge_id]
        if source is not None and source != edge.source:
            return edge.reversal
        else:
            return edge

    #頂点vを含む連結成分
    def connected_component(self, v: int) -> list[int]:
        """ 頂点 v を含む連結成分を求める.

        Args:
            v (int): 頂点

        Returns:
            list[int]: 頂点 v を含む連結成分に含まれる頂点番号のリスト
        """

        stack = [v]
        comp = [False] * len(self.adjacent); comp[v] = True
        while stack:
            x = stack.pop()
            for edge in self.adjacent[x]:
                y = edge.target
                if comp[y]:
                    continue

                comp[y] = True
                stack.append(y)

        return [x for x in range(len(self.adjacent)) if comp[x]]

    #距離
    def distance(self, u: int, v: int, default = -1) -> int:
        """ 2 頂点 u, v の距離を求める (存在しない場合は default)

        Args:
            u (int): 始点
            v (int): 終点
            default (int, optional): uv Path が存在しない場合の返り値. Defaults to -1.

        Returns:
            int: u, v 間の距離
        """
        from collections import deque

        if u == v:
            return 0

        dist = [-1] * self.order
        dist[u] = 0

        queue = deque([u])
        while queue:
            x = queue.popleft()
            for edge in self.adjacent[x]:
                y = edge.target
                if dist[y] != -1:
                    continue

                dist[y] = dist[x] + 1
                queue.append(y)

                if y == v:
                    return dist[v]

        return default

    #ある1点からの距離
    def distance_all(self, u: int, default = -1) -> list[int]:
        """ 全ての頂点について, 頂点 u からの距離を求める (u と非連結な場合は default になる).

        Args:
            u (int): 始点となる頂点
            default (int, optional): 頂点 u と連結でない場合の格納値. Defaults to -1.

        Returns:
            list[int]: 第 v 要素は u, v 間の距離 (u, v が連結でない場合は default)
        """

        from collections import deque

        dist = [-1] * self.order
        dist[u] = 0

        queue = deque([u])
        while queue:
            x = queue.popleft()
            for edge in self.adjacent[x]:
                y = edge.target
                if dist[y] != -1:
                    continue

                dist[y] = dist[x] + 1
                queue.append(y)

        return [dist[x] if dist[x] != -1 else default for x in range(self.order)]

    #最短路
    def shortest_path(self, u: int, v: int) -> list[Edge]:
        """ 頂点 u から頂点 v への最短路を求める (存在しない場合は None)

        Args:
            u (int): 始点
            v (int): 終点

        Returns:
            list[int]: 頂点 u から頂点 v への最短路. 存在しない場合は None
        """

        if u == v:
            return []

        from collections import deque

        prev: list[Edge] = [None] * self.order
        prev[u] = u

        queue = deque([u])
        while queue:
            x = queue.popleft()
            for edge in self.adjacent[x]:
                y = edge.target

                if prev[y] is not None:
                    continue

                prev[y] = edge
                queue.append(y)

            if prev[v] is not None:
                break

        if prev[v] is None:
            return None

        path: list[Edge] = []
        a = v
        while a != u:
            edge = prev[a]
            path.append(edge)
            a = edge.source
        return path[::-1]

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
    total_order = sum(G.order for G in Graphs)
    order_offset = 0

    H = Graph(total_order)
    for G in Graphs:
        for u, v, t in G.edge_yielder():
            H.add_edge(u + order_offset, v + order_offset, t)
        order_offset += G.order

    return H

#==========
#連結グラフ?
def Is_Connected(G: Graph):
    """ G は連結グラフ ?

    Args:
        G (Graph)
    """

    return (G.order == 0) or all(d >= 0 for d in G.distance_all(0))

#=====
#森?
def Is_Forest(G: Graph):
    """ 森かどうか判定する. """

    return G.order == G.size + Connected_Component_Number(G)

#木?
def Is_Tree(G: Graph):
    """ 木かどうか判定する. """
    return (G.size == G.order - 1) and Is_Connected(G)

#木の直径
def Tree_Diameter(T: Graph, Mode = False):
    """ 木 T の直径を求める.

    T: 木

    (出力の結果)
    Mode=True → (直径, (直径を成す端点1, 直径を成す端点2))
    Mode=False → 直径
    """

    def bfs(x):
        dist = [-1] * T.order; dist[x] = 0
        stack = [x]
        while stack:
            u = stack.pop()

            for v in T.neighborhood(u):
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    stack.append(v)

        y = max(range(T.order), key = lambda x: dist[x])
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


    group = [-1] * G.order
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
    for x in range(G.order):
        if group[x] == -1:
            dfs(x, g)
            g += 1

    return { 'components': comps, 'group': group }

#連結成分の個数
def Connected_Component_Number(G: Graph):
    """ 連結成分の個数を求める. """

    seen = [False] * G.order

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
    for x in range(G.order):
        if not seen[x]:
            count += 1
            bfs(x)

    return count

#2部グラフ?
def Is_Bipartite_Graph(G: Graph):
    """ 2部グラフかどうかを判定する. """

    seen = [0] * G.order

    for v in range(G.order):
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

    N = G.order
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

#ハミルトングラフ?
def Is_Hamiltonian_Graph(G):
    """ ハミルトングラフ (全ての頂点を1回ずつ通るサイクルを含むグラフ) かどうかを判定する.

    """
    pass

#ハミルトンを探す.
def Find_Hamiltonian_Graph(G):
    pass

#クリーク
def Clique(G: Graph, calc, merge, unit, empty = False):
    """
    グラフ G に対する Clique C 全てに対する calc(C) を計算し, merge でマージする.

    G: Graph
    calc: calc(C) Clique である部分集合 C に対する値
    merge: merge(x,y) x,y のマージの方法
    empty: 空集合を Clique とするか?

    計算量: O(2^{sqrt(2M)} N)
    """

    N=G.order; M=G.size
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
def Triangle(G: Graph, calc, merge, unit):
    """
    calc: calc(i,j,k) 3頂点 i,j,k からなる頂点に対する値
    merge: merge(x,y) x,y のマージの方法
    unit: 単位元

    計算量: O(M sqrt(2M))
    """

    N=G.order
    A=[[] for _ in range(N)]

    deg=G.degree
    for i in range(N):
        for j in G.partner_yield(i):
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

#グラフ作成
def Making_Graph(N,E):
    """ 辺の情報 E からグラフを生成する. """

    G=Graph(N)
    for e in E:
        G.add_edge(*e)
    return G

#Cycleグラフ
def Cycle_Graph(N):
    """ N 頂点からなるサイクルグラフを生成する. """

    C=Graph(N)
    for i in range(N):
        C.add_edge(i, (i+1)%N)
    return C

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

    N=G.order
    adj=[list(a) for a in G.adjacent]
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
