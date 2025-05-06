class Weighted_Edge:
    __slots__ = ("__id", "__source", "__target", "__weight", "__reversal")

    def __init__(self, id: int, source: int, target: int, weight: int):
        self.__id = id
        self.__source = source
        self.__target = target
        self.__weight = weight
        self.__reversal: Weighted_Edge = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, source={self.source}, target={self.target}, weight={self.weight})"

    def fetch_reversal_edge(self) -> "Weighted_Edge":
        reversal_edge = Weighted_Edge(self.id, self.target, self.source, self.weight)
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
    def weight(self) -> int:
        return self.__weight

    @property
    def reversal(self) -> "Weighted_Edge":
        return self.__reversal

class Weighted_Graph:
    #入力定義
    def __init__(self, N: int = 0, edge_offset: int = 0):
        """ 重みあり無向グラフを生成する.

        Args:
            N (int, optional): 位数. Defaults to 0.
            edge_offset (int, optional): 辺のオフセット. Defaults to 0.
        """

        self.adjacent: list[list[Weighted_Edge]] = [[] for _ in range(N)]
        self.__edge_count: int = 0
        self.__edge_offset = edge_offset
        self.__ininity: int = 0

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

    @inifinity.setter
    def inifinity(self, value):
        self.__ininity = value

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
    def add_edge(self, u: int, v: int, weight: int = 1) -> int:
        id = self.__edge_offset + self.edge_count

        edge = Weighted_Edge(id, u, v, weight)
        self.adjacent[u].append(edge)

        if u != v:
            edge.fetch_reversal_edge()
            self.adjacent[v].append(edge.reversal)

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

    def initialize_list(self, x) -> list:
        return [x] * self.vertex_count

#Dijkstra
def Dijkstra(G: Weighted_Graph, start: int, goal: int, with_path: bool = False) -> dict:
    """ 頂点 start から頂点 goal への最短路の距離を求める.

    Args:
        G (Weighted_Graph): 重み付き有向グラフ
        start (int): 始点
        goal (int): 終点
        with_path (bool, optional): True にすると, 最短路も求める.. Defaults to False.

    Returns:
        dict:
            dist: source → target 間の距離
            path: 最短路のパス
    """

    from heapq import heappush,heappop

    inf = float("inf")
    adj = G.adjacent

    dist: list[int] = G.initialize_list(inf); dist[start] = 0
    prev: list[Weighted_Edge] = G.initialize_list(None)
    fix: list[bool] = G.initialize_list(False)

    Q = [(0, start)]

    while Q:
        d, v = heappop(Q)

        if v == goal:
            break

        if fix[v]:
            continue

        fix[v] = True

        for edge in adj[v]:
            t = edge.target
            if not dist[t] > d + edge.weight:
                continue

            dist[t] = dist[v] + edge.weight
            heappush(Q, (dist[t], t))
            prev[t] = edge

    if (dist[goal] == inf) or (not with_path):
        return { 'dist': dist[goal], 'path': None}

    path = []
    x = goal
    while (edge := prev[x]) is not None:
        path.append(edge)
        x = edge.source

    path.reverse()
    return { 'dist': dist[goal], 'path': path }

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
def Warshall_Floyd(G: Weighted_Edge) -> list[list[int]]:
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
def Tree_Diameter(T: Weighted_Graph) -> dict:
    """ 木 T の直径及び直径をなすパスを求める.

    Args:
        T (Weighted_Graph): 木

    Returns:
        dict:
            diameter: 直径
            path: 直径をなすパス
    """

    def bfs(x: int, mode: bool):
        dist = [None] * N; dist[x] = 0
        stack = [x]
        prev: list[Weighted_Edge] = [None] * N

        while stack:
            x = stack.pop()
            for edge in T.adjacent[x]:
                if dist[edge.target] is not None:
                    continue

                dist[edge.target] = dist[x] + edge.weight
                stack.append(edge.target)
                prev[edge.target] = edge

        furthest = max(range(N), key = lambda v: dist[v])
        if not mode:
            return furthest

        path: list[Weighted_Edge] = []
        v = furthest
        while (edge := prev[v]) is not None:
            path.append(edge)
            v = edge.source

        path.reverse()
        return dist[furthest], path

    N = T.vertex_count
    u = bfs(0, False)
    diameter, path = bfs(u, True)

    return { 'diameter': diameter, 'path': path }
