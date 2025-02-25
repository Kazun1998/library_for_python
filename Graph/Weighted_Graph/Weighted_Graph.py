class Weigthed_Graph:
    #入力定義
    def __init__(self, N: int = 0):
        """ 重みあり無向グラフを生成する.

        Args:
            N (int, optional): 位数. Defaults to 0.
        """

        self.adjacent = [[] for _ in range(N)]
        self.__edge_count = 0
        self.__ininity = 0

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
        """ 辺の本数 (サイズ) を出力する.

        Returns:
            int: 辺の本数
        """
        return self.__edge_count

    @property
    def size(self) -> int:
        """ サイズ (辺の本数) を出力する.

        Returns:
            int: サイズ
        """
        return self.__edge_count

    @property
    def inifinity(self) -> int:
        return self.__ininity

    #頂点の追加
    def add_vertex(self):
        """ 頂点を追加する.

        """
        self.adjacent.append({})
        return self.order - 1

    def add_vertices(self, k):
        """ 頂点を k 個追加する.

        k: int
        """

        n = self.order
        self.adjacent.extend([[]for _ in range(k)])
        return list(range(n, n + k))

    #辺の追加
    def add_edge(self, u: int, v: int, weight: int = 1, label = None):
        """ 重さが weight の辺 uv を加える. """

        self.adjacent[u].append((v, weight, label))
        self.adjacent[v].append((u, weight, label))
        self.__edge_count += 1
        self.__ininity += 2 * max(1, weight)
        return id

    #頂点を除く

    #Walkの追加

    #Cycleの追加

    #頂点の交換

    #グラフに辺が存在するか否か
    def edge_exist(self, u, v):
        pass

    #近傍
    def neighbohood(self,v):
        pass

    def edge_yielder(self):
        generated = set()
        for u in range(self.order):
            for v, w, id in self.adjacent[u]:
                if id not in generated:
                    generated.add(id)
                    yield (u, v, w, id)


#Dijkstra
def Dijkstra(G, From, To, with_path=False):
    """ Dijksta 法を用いて, From から To までの距離を求める.

    G: 辺の重みが全て非負の無向グラフ
    From: 始点
    To: 終点
    with_path: 最短路も含めて出力するか?

    (出力の結果)
    with_path=True  →(距離, 最短経路の辿る際の前の頂点)
    with_path=False →距離
    """
    from heapq import heappush,heappop

    inf=float("inf")
    N=G.vertex_count
    adj=G.adjacent

    T=[inf]*N; T[From]=0

    if with_path:
        Prev=[-1]*N

    Q=[(0,From)]

    while Q:
        c,u=heappop(Q)

        if u==To:
            break

        if T[u]<c:
            continue

        E=adj[u]
        for v in E:
            p=T[u]+E[v]
            if T[v]>p:
                T[v]=p
                heappush(Q,(p,v))

                if with_path:
                    Prev[v]=u

    if T[To]==inf:
        if with_path:
            return (inf,None)
        else:
            return inf

    if with_path:
        path=[To]
        u=To
        while (Prev[u]!=None):
            u=Prev[u]
            path.append(u)
        return (T[To],path[::-1])
    else:
        return T[To]

def Dijkstra_All(G, From, with_path=False):
    """ Dijksta 法を用いて, From から各頂点までの距離を求める.

    G: 辺の重みが全て非負の無向グラフ
    From: 始点
    with_path: 最短路も含めて出力するか?

    (出力の結果)
    with_path=True  → (距離のリスト, 最短経路の辿る際の前の頂点)
    with_path=False → 距離のリスト
    """
    from heapq import heappush,heappop

    inf=float("inf")
    N=G.vertex_count
    adj=G.adjacent

    T=[inf]*N; T[From]=0

    if with_path:
        Prev=[-1]*N

    Q=[(0,From)]

    while Q:
        c,u=heappop(Q)

        if T[u]<c:
            continue

        E=adj[u]
        for v in E:
            p=T[u]+E[v]
            if T[v]>p:
                T[v]=p
                heappush(Q,(p,v))

                if with_path:
                    Prev[v]=u

    if with_path:
        return (T,Prev)
    else:
        return  T

#Warshall–Floyd
def Warshall_Floyd(G: Weigthed_Graph) -> list[list[int]]:
    """ Warshall-Floyd 法を用いて, 全点間距離を求める.

    Args:
        G (Weigthed_Graph): 無向グラフ

    Returns:
        list[list[int]]: (i, j) 成分が i, j 間の距離. ただし, 負の閉路による影響を受ける場合は -inf
    """

    def three_loop():
        for u, du in enumerate(dist):
            for _, dv in enumerate(dist):
                for w in range(N):
                    dv[w] = min(dv[w], dv[u] + du[w])

    inf = G.inifinity
    N = G.vertex_count

    dist = [[0 if i == j else inf for j in range(N)] for i in range(N)]
    for u in range(N):
        dist_u = dist[u]
        for v, w, _ in G.adjacent[u]:
            dist_u[v] = min(dist_u[v], w)

    three_loop()

    if any(dist[v][v] < 0 for v in range(N)):
        for v in range(N):
            if dist[v][v] < 0:
                dist[v][v] = - float('inf')
        three_loop()

    return dist

#巡回セールスマン問題を解く.
def Traveling_Salesman_Problem(G):
    N=G.vertex_count

    inf=float("inf")
    T=[[inf]*N for _ in range(1<<N)]
    T[0][0]=0

    for S in range(1<<N):
        F=T[S]
        for v in range(N):
            if S&(1<<v):
                continue

            E=T[S|1<<v]
            cost=G.adjacent[v]

            for w,c in cost.items():
                if v!=w and G.edge_exist(v,w) and E[v]>F[w]+c:
                    E[v]=F[w]+c
    return T[-1][0]

# 木の直径を求める.
def Tree_Diameter(T: Weigthed_Graph):
    """ 木 T の直径及び, 直径をなすパスを返す.

    Args:
        T (Weigthed_Graph): 木
    """

    def bfs(x: int, mode: bool):
        dist = [-1] * N; dist[x] = 0
        adj = T.adjacent
        S = [x]
        prev = [-1] * N

        while S:
            x = S.pop()
            for y, c, _ in adj[x]:
                if dist[y] == -1:
                    dist[y] = dist[x] + c
                    S.append(y)
                    prev[y] = x

        furthest = max(range(N), key = lambda v: dist[v])
        if not mode:
            return furthest

        path = [furthest]
        v = furthest
        while prev[v] != -1:
            v = prev[v]
            path.append(v)

        return dist[furthest], path[::-1]

    N = T.vertex_count
    u = bfs(0, False)
    diameter, path = bfs(u, True)

    return { 'diameter': diameter, 'path': path }
