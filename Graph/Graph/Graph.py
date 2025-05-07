class Edge:
    def __init__(self, id: int, source: int, target: int):
        self.__id = id
        self.__source = source
        self.__target = target

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, source={self.source}, target={self.target})"

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

    def edge_generator(self):
        for i in range(self.__edge_offset, self.__edge_offset + self.size):
            yield self.edges[i]

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
def Is_Connected(G: Graph) -> bool:
    """ G は連結グラフ (0 頂点のグラフは連結とする) ?

    Args:
        G (Graph): 無向グラフ

    Returns:
        bool: 連結グラフ ?
    """

    return (G.order == 0) or all(d >= 0 for d in G.distance_all(0))

#=====
#森?
def Is_Forest(G: Graph) -> bool:
    """ グラフ G が森 (サイクルを持たない) かどうかを判定する.

    Args:
        G (Graph): 無向グラフ

    Returns:
        bool: 森?
    """

    return G.order == G.size + Connected_Component_Number(G)

#木?
def Is_Tree(G: Graph) -> bool:
    """ G が木 (連結な森) かどうかを判定する.

    Args:
        G (Graph): 無向グラフ

    Returns:
        bool: 木?
    """

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
def Connected_Component_Decomposition(G: Graph) -> dict[str, list[int]]:
    """ 無向グラフ G を連結成分毎に分割する.

    Args:
        G (Graph): 無向グラフ

    Returns:
        dict[str, list[int]]: 'components', 'group' をキーに持つ辞書
            'components': "各要素が連結成分であるリスト"のリスト
            'group': 長さが位数のリストであり, 「頂点 x と頂点 y が同じ連結成分 iff group[x] == group[y]」を満たす
    """

    group = [None] * G.order
    components = []

    def dfs(start: int, g: int):
        """ start から DFS を行い, 到達した頂点にラベル g を付与する.

        Args:
            start (int): 開始の頂点
            g (int): ラベル
        """

        stack = [start]
        group[start] = g
        component = []

        while stack:
            x = stack.pop()
            component.append(x)
            for y in G.partner_yield(x):
                if group[y] == -1:
                    group[y] = g
                    stack.append(y)
        components.append(component)

    g = 0
    for x in range(G.order):
        if group[x] is not None:
            continue

        dfs(x, g)
        g += 1

    return { 'components': components, 'group': group }

#連結成分の個数
def Connected_Component_Number(G: Graph) -> int:
    """ 無向グラフ G の連結成分の数を求める.

    Args:
        G (Graph): 無向グラフ

    Returns:
        int: 連結成分の数
    """

    seen = [False] * G.order

    def bfs(start: int):
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
def Is_Bipartite_Graph(G: Graph) -> bool:
    """ G は二部グラフ ?

    Args:
        G (Graph): 無向グラフ

    Returns:
        bool: 二部グラフ ?
    """

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
def Bipartite_Separate(G: Graph) -> list[tuple[list[int], list[int]]]:
    """ 二部グラフ G を部集合に分割する.

    Args:
        G (Graph): 無向グラフ

    Returns:
        list[tuple[list[int], list[int]]]: [(A0, B0), (A1, B1), ..., (Ak, Bk)] の形のリスト
            i = 0, 1, ..., k に対して, Ai と Bi は同じ連結成分に属し, Ai, Bi がそれぞれの部集合になる
    """

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

            for edge in G.adjacent[u]:
                w = edge.target
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
def Clique(G: Graph, calc, merge, unit, empty: bool = False):
    """ グラフ G における Clique 全てに対する calc(C) を計算し, その結果を merge でマージする.

    Args:
        G (Graph): 無向グラフ (単純グラフを想定)
        calc (Callable[[list[int]], X]): Clique
        merge (Callable[[X, X], X]): 結果をマージする演算
        unit (X): X の単位元
        empty (bool, optional): 空グラフを Clique として認めるか?. Defaults to False.

    Returns:
        X:

    計算量: O(2^{sqrt(2M)} N)
    """

    N = G.order
    M = G.size
    deg = [G.degree(v) for v in range(N)]
    arrival = [True] * N

    threshold = 0
    while pow(threshold, 2) <= 2 * M:
        threshold += 1

    F = [[0] * N for _ in range(N)]
    for edge in G.edge_generator():
        u = edge.source
        v = edge.target
        F[u][v] = F[v][u] = 1

    res = unit
    while True:
        A = []

        # 次数が sqrt(2M) 以下で残っている頂点 u を探す
        for u in range(N):
            if not(arrival[u] and deg[u] < threshold):
                continue

            for v in range(N):
                if u != v and arrival[v] and F[u][v]:
                    A.append(v)
            A.append(u)
            break
        else:
            break

        # 頂点 u に接続している頂点についてを計算する
        K = len(A) - 1
        bit = [0] * K # bit[i] の j ビット目が 1 iff A[i] と A[j] は隣接して"いない"

        for i in range(K):
            for j in range(i):
                if not F[A[i]][A[j]]:
                    bit[i] |= 1 << j
                    bit[j] |= 1 << i

        # 頂点 u に接続している頂点の可能性 (2^K 通り) を全探索する
        for S in range(1<<K):
            flag = True
            for i in range(K):
                if (S >> i) & 1:
                    flag &= (S & bit[i] == 0)

            if not flag:
                continue

            # 頂点 u と [A[x] for x in S] が Clique になる
            clique = [A[i] for i in range(K) if (S >> i) & 1]
            clique.append(A[-1])

            res = merge(res, calc(clique))

        # 頂点 u を削除する
        arrival[A[-1]] = False
        deg[A[-1]] = 0
        for v in range(N):
            if A[-1] != v and arrival[v] and F[A[-1]][v]:
                deg[v] -= 1

    # 残りの頂点についてを探索する (残っている頂点は sqrt(2M) 個以下)
    A = [u for u in range(N) if arrival[u]]

    K = len(A)
    bit = [0] * K
    for i in range(K):
        for j in range(i):
            if not F[A[i]][A[j]]:
                bit[i] |= 1 << j
                bit[j] |= 1 << i

    for S in range(1 << K):
        if S == 0:
            # 空グラフに関する処理を別個で行う
            if empty:
                res = merge(res, calc([]))
            continue

        flag = True
        for i in range(K):
            if (S >> i) & 1:
                flag &= (S & bit[i] == 0)

        if not flag:
            continue

        clique = [A[i] for i in range(K) if (S >> i) & 1]
        res = merge(res, calc(clique))

    return res

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
def Making_Graph(N: int, edges: list[tuple[int, int]], edge_offset: int = 0) -> Graph:
    """ 位数 N のグラフで辺のリスト edges からグラフを生成する.

    Args:
        N (int): 位数
        edges (list[tuple[int, int]]): (u, v) のリスト. 1 つの要素が辺 uv に対応する.
        edge_offset (int, optional): 辺番号のオフセット. Defaults to 0.

    Returns:
        Graph: 無向グラフ
    """

    G = Graph(N, edge_offset)
    for edge in edges:
        G.add_edge(*edge)
    return G

#==========
# グラフの走査
#==========
def Depth_First_Search(G: Graph):
    """ 無向グラフ G に対して, 深さ優先探索の移動を generate する.

    Args:
        G (Graph): 無向グラフ.

    Notes:
        各要素は (u, v, d, edge) の形
            (-1, v,  1, None): v が探索開始の頂点である.
            (u,  v,  1, edge): u から v へ向かう辺で, DFS 木で葉に進む向きになる辺
            (u,  v,  0, edge): u から v へ向かう辺で後退辺 (DFS 木には不採用)
            (u,  v, -1, edge): u から v へ向かう辺で, DFS 木では根に進む向きになる辺
            (u, -1, -1, None): u から始まった DFS が終了
    """

    N = G.order
    seen = [False] * N
    progess = [0] * N
    parent: list[int] = [None] * N
    upper_edge: list[Edge] = [None] * N

    def dfs(start: int):
        stack = [start]

        # 探索開始
        yield (None, start, 1, None)
        while stack:
            x = stack.pop()
            seen[x] = True

            while progess[x] < len(G.adjacent[x]):
                edge = G.adjacent[x][progess[x]]
                y = edge.target
                progess[x] += 1

                if (upper_edge[x] is not None) and (upper_edge[x].id == edge.id):
                    continue

                if not seen[y]:
                    # 前進辺
                    stack.append(x)
                    stack.append(y)
                    parent[y] = x
                    upper_edge[y] = edge
                    yield (x, y, 1, edge)
                    break
                else:
                    # 後退辺
                    yield (x, y, 0, edge)
            else:
                # 親に戻る
                if parent[x] is not None:
                    yield (x, parent[x], -1, upper_edge[x])

        # 探索終了
        yield (start, None, -1, None)

    for x in range(N):
        if not seen[x]:
            yield from dfs(x)

#==================================================
# Cycle
def Is_Exist_Cycle(G: Graph) -> bool:
    """ 単純無向グラフ G にサイクルは存在する ?

    Args:
        G (Graph): 単純無向グラフ

    Returns:
        bool: サイクルは存在する?
    """
    return G.order < G.size + Connected_Component_Number(G)

def Find_Cycle(G: Graph) -> list[Edge]:
    """ G におけるサイクルを見つける (存在しない場合は None)

    Args:
        G (Graph): グラフ

    Returns:
        list[int]: サイクル (存在しない場合は None)
    """

    N = G.order

    seen = [False] * N
    upper = [None] * N

    # DFS 木における後退辺があれば, その後退辺を含むサイクルが存在する.
    def find_cycle(start: int) -> list[Edge]:
        seen[start] = True
        stack = [edge for edge in G.adjacent[start]]

        while stack:
            edge = stack.pop()

            u = edge.source
            v = edge.target

            if seen[v]:
                back_edge = edge
                break

            seen[v] = True
            upper[v] = edge

            edge_id = edge.id
            stack.extend([e for e in G.adjacent[v] if e.id != edge_id])
        else:
            return None

        cycle = [back_edge]
        u = back_edge.source
        while u != v:
            edge = upper[u]
            cycle.append(edge)
            u = edge.source
        return cycle

    for x in range(N):
        if seen[x]:
            continue

        cycle = find_cycle(x)
        if cycle is not None:
            cycle.reverse()
            return cycle

    return None
