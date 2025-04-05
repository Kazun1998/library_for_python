class Arc:
    def __init__(self, id: int, source: int, target: int):
        self.__id = id
        self.__source = source
        self.__target = target

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, source={self.source}, target={self.target})"

    @property
    def id(self) -> int:
        return self.__id

    @property
    def source(self) -> int:
        return self.__source

    @property
    def target(self) -> int:
        return self.__target

class Digraph:
    """重み[なし]有向グラフを生成する.

    """

    #入力定義
    def __init__(self, N = 0, arc_offset: int = 0):
        """ N 頂点の有向グラフを生成する.

        Args:
            N (int, optional): 頂点数. Defaults to 0.
            arc_offset (int, optional): 弧の番号のオフセット. Defaults to 0.
        """

        self.adjacent_out: list[list[Arc]] = [[] for _ in range(N)] # 出近傍 (v が始点)
        self.adjacent_in: list[list[Arc]] = [[] for _ in range(N)] # 入近傍 (v が終点)
        self.__arc_offset = arc_offset
        self.__arcs: list[Arc] = [None] * arc_offset

    # propertry
    @property
    def order(self) -> int:
        """ グラフの位数 (頂点数) を出力する.

        Returns:
            int: 位数
        """
        return len(self.adjacent_out)

    @property
    def vertex_count(self):
        """ グラフの頂点数 (位数) を出力する.

        Returns:
            int: 頂点数
        """
        return len(self.adjacent_out)

    @property
    def size(self):
        """ グラフのサイズ (辺の本数) を出力する.

        Returns:
            int: サイズ
        """
        return len(self.__arcs) - self.__arc_offset

    @property
    def arc_count(self):
        """ グラフの辺の本数 (サイズ) を出力する.

        Returns:
            int: 辺の本数
        """
        return len(self.__arcs) - self.__arc_offset

    #頂点の追加
    def add_vertex(self):
        """ 頂点を追加する.

        """
        self.adjacent_out.append([])
        self.adjacent_in.append([])
        return self.order - 1

    def add_vertices(self, k = 1):
        """ 頂点を k 個追加する.

        k: int
        """
        n = self.order
        self.adjacent_out.extend([[] for _ in range(k)])
        self.adjacent_in.extend([[] for _ in range(k)])
        return list(range(n, n + k))

    # 弧の追加
    def add_arc(self, source: int, target: int) -> int:
        """ source から target への弧を追加する.

        Args:
            source (int): 始点
            target (int): 終点

        Returns:
            int: 追加した弧の id
        """

        id = len(self.__arcs)
        arc = Arc(id, source, target)
        self.adjacent_out[source].append(arc)
        self.adjacent_in[target].append(arc)
        self.__arcs.append(arc)

        return arc

    # Walk の追加
    def add_walk(self, *walk: int) -> list[int]:
        """ 有向歩道 walk = (w[0], w[1], .., w[k - 1]) を追加する.

        Returns:
            list[int]: 追加した (k - 1) 個の弧の id 番号からなる配列
        """

        return [self.add_arc(walk[i], walk[i + 1]) for i in range(len(walk) - 1)]

    # Cycle の追加
    def add_cycle(self, *cycle) -> list[int]:
        """ 有向歩道 cycle = (c[0], c[1], .., c[k - 1], c[0]) を追加する.

        Returns:
            list[int]: 追加した k 個の弧の id 番号からなる配列
        """

        if len(cycle) == 0:
            return []

        arc_ids = self.add_walk(*cycle)
        arc_ids.append(cycle[-1], cycle[0])
        return arc_ids

    def get_arc(self, id: int) -> Arc:
        return self.__arcs[id]

    # 出次数
    def out_degree(self, v: int) -> int:
        """ 出次数 (頂点 v から出る弧の本数)

        Args:
            v (int): 頂点

        Returns:
            int: 出次数
        """
        return len(self.adjacent_out[v])

    # 入次数
    def in_degree(self,v) -> int:
        """ 入次数 (頂点 v に入る弧の本数)

        Args:
            v (int): 頂点

        Returns:
            int: 入次数
        """
        return len(self.adjacent_in[v])

    # 次数
    def degree(self,v):
        return (self.out_degree(v), self.in_degree(v))

    # 相対次数
    def relative_degree(self, v: int) -> int:
        """ 頂点 v における (出次数) - (入次数) を求める.

        Args:
            v (int): 頂点

        Returns:
            int: (出次数) - (入次数)
        """

        return self.out_degree(v) - self.in_degree(v)

    # 頂点 v に到達可能な頂点
    def reachable_to(self, v: int) -> list[int]:
        """ 頂点 v に到達可能な頂点を求める.

        Args:
            v (int): 終点となる頂点

        Returns:
            list[int]: 頂点 v に到達可能な頂点のリスト
        """

        reach = [False] * self.order; reach[v] = True
        stack = [v]

        while stack:
            x = stack.pop()

            for arc in self.adjacent_in[x]:
                y = arc.source

                if reach[y]:
                    continue

                reach[y] = True
                stack.append(y)

        return [x for x in range(self.order) if reach[x]]

    # 頂点 v から到達可能な頂点
    def reachable_from(self, v: int) -> list[int]:
        """ 頂点 v から到達可能な頂点を求める.

        Args:
            v (int): 始点となる頂点

        Returns:
            list[int]: 頂点 v から到達可能な頂点のリスト
        """

        reach = [False] * self.order; reach[v] = True
        stack = [v]

        while stack:
            x = stack.pop()

            for arc in self.adjacent_out[x]:
                y = arc.source

                if reach[y]:
                    continue

                reach[y] = True
                stack.append(y)

        return [x for x in range(self.order) if reach[x]]

    # 頂点 u,v の距離を求める.
    def distance(self, u: int, v: int, default = -1) -> int:
        """ 頂点 u から頂点 v への距離を求める.

        Args:
            u (int): 始点
            v (int): 終点
            default (int, optional): 存在しない場合の返り値. Defaults to -1.

        Returns:
            int: 距離
        """

        from collections import deque

        dist = [-1] * self.order
        dist[u] = 0

        queue = deque([u])
        while queue:
            x = queue.popleft()
            for arc in self.adjacent_out[x]:
                y = arc.target

                dist[y] = dist[x] + 1
                queue.append(y)

                if y == v:
                    return dist[y]

        return default

    #ある1点からの距離
    def distance_all(self, u, default):
        """ 頂点 u からの距離をそれぞれの頂点について求める."""

        from collections import deque

        dist = [-1] * self.vertex_count()
        dist[u] = 0

        Q = deque([u])
        while Q:
            x = Q.popleft()
            for y in self.in_partner_yield(x):
                if dist[y] != -1:
                    continue

                dist[y] = dist[x] + 1
                Q.append(y)

        return [d if d != -1 else default for d in dist]

    def shortest_path(self, u: int, v: int) -> list[Arc]:
        """ 頂点 u から頂点 v への最短路を求める.

        Args:
            u (int): 始点
            v (int): 終点

        Returns:
            list[Arc]: 最短路 (存在しない場合は None)
        """

        if u == v:
            return []

        from collections import deque

        prev: list[Arc] = [None] * self.order

        Q = deque([u])

        while Q and (prev[v] is None):
            x = Q.popleft()
            for arc in self.adjacent_out[x]:
                y = arc.target

                if prev[y] is not None:
                    continue

                prev[y] = arc
                Q.append(y)

        if prev[v] is None:
            return None

        path: list[Arc] = []
        while v != u:
            arc = prev[v]
            path.append(arc)
            v = arc.source

        path.reverse()
        return path

#逆グラフの作成
def Inverse_Graph(D):
    """有向グラフDの全ての辺の向きを変えたグラフを出力する.

    D:有向グラフ
    """
    E=D.deepcopy()
    E.adjacent_out,E.adjacent_in=E.adjacent_in,E.adjacent_out
    return E

# Topological Sort
def Topological_Sort(D: Digraph) -> list[int]:
    """ D の Topological Sort を求める

    Args:
        D (Digraph): 有向グラフ

    Returns:
        list[int]: Topological Sort (存在しない場合は None)
    """

    remain = [D.in_degree(x) for x in range(D.order)]
    candidates = [v for v in range(D.order) if remain[v] == 0]

    sort = []
    while candidates:
        u = candidates.pop()
        sort.append(u)
        for arc in D.adjacent_out[u]:
            v = arc.target
            remain[v] -= 1

            if remain[v] == 0:
                candidates.append(v)

    return sort if len(sort) == D.order else None

#DAG?
def Is_Directed_Acyclic_Graph(D: Digraph) -> bool:
    """ D は DAG ?

    Args:
        D (Digraph): 有向グラフ

    Returns:
        bool: DAG ?
    """

    remain = [D.in_degree(x) for x in range(D.order)]
    stack = [v for v in range(D.order) if remain[v] == 0]

    for _ in range(D.order):
        if not stack:
            return False

        u = stack.pop()
        for v in D.adjacent_out[u]:
            remain[v] -= 1

            if remain[v] == 0:
                stack.append(v)
    return True

#Cycleを縮約
def Cycle_Reduction(D):
    C=Strongly_Connected_Component_Decomposition(D,1)

    E=Digraph(max(C)+1)
    for v in range(D.vertex_count()):
        for w in D.adjacent_out[v]:
            if C[v]!=C[w]:
                E.add_arc(C[v],C[w])
    return E

#強連結成分に分解
def Strongly_Connected_Component_Decomposition(D,Mode=0):
    """有向グラフDを強連結成分に分解

    Mode:
    0(Defalt)---各強連結成分の頂点のリスト
    1        ---各頂点が属している強連結成分の番号
    2        ---0,1の両方

    ※0で帰ってくるリストは各強連結成分に関してトポロジカルソートである.
    """

    N=D.vertex_count()
    Group=[0]*N
    Order=[]
    adj_out=D.adjacent_out; adj_in=D.adjacent_in

    for v in range(N):
        if Group[v]==-1:
            continue

        S=[v]
        Group[v]=-1

        while S:
            u=S.pop()
            for w in adj_out[u]:
                if Group[w]:
                    continue

                Group[w]=-1
                S.append(u)
                S.append(w)
                break
            else:
                Order.append(u)

    k=0
    for v in Order[::-1]:
        if Group[v]!=-1:
            continue

        S=[v]
        Group[v]=k

        while S:
            u=S.pop()
            for w in adj_in[u]:
                if Group[w]!=-1:
                    continue

                Group[w]=k
                S.append(w)
        k+=1

    if Mode==0 or Mode==2:
        T=[[] for _ in range(k)]
        for v in range(N):
            T[Group[v]].append(v)

    if Mode==0:
        return T
    elif Mode==1:
        return Group
    else:
        return (Group,T)

#強連結成分の代表元
def Strongly_Connected_Component_Representative(D):
    X=Strongly_Connected_Component_Decomposition(D)
    return [C[0] for C in X]

#強連結成分の個数
def Strongly_Connected_Component_Number(D):
    """有向グラフDの強連結成分の個数

    """
    return len(Strongly_Connected_Component_Decomposition(D))

#誘導グラフ
def Induced_Subgraph(D,S):
    """ 以下を満たすようなグラフ D' を生成する.
    V(D')=V(D), st in A(D') iff st in A(D), s,t in S

    D: 有向グラフ
    S: 頂点集合
    """
    S=set(S)

    N=D.vertex_count()
    E=Digraph(N); adj_out=D.adjacent_out

    for s in range(N):
        if s not in S:
            continue

        for t in adj_out[s]:
            if t in S:
                E.add_arc(s,t)
    return E

#Cycleが存在する?
def Is_Exist_Cycle(D):
    return not Is_Directed_Acyclic_Graph(D)

#Cycleを見つける.
#参考元:https://judge.yosupo.jp/submission/23992
def Find_Cycle(D):
    from collections import deque

    N=D.vertex_count()
    in_deg=[D.in_degree(v) for v in range(N)]
    adj_out=D.adjacent_out
    Q=deque([v for v in range(N) if in_deg[v]==0])

    while Q:
        v=Q.popleft()
        for w in adj_out[v]:
            in_deg[w]-=1
            if in_deg[w]==0:
                Q.append(w)

    for v in range(N):
        P=[]
        if in_deg[v]==0:
            continue

        Q=deque([v])
        prev=[-1]*N
        while Q:
            x=Q.popleft()
            for y in adj_out[x]:
                if y==v:
                    prev[v]=x
                    break
                if prev[y]!=-1:
                    continue

                prev[y]=x
                Q.append(y)
            else:
                continue
            break
        else:
            continue
        P=[v]
        x=v
        while prev[x]!=v:
            x=prev[x]
            P.append(x)
        break
    if P:
        return P[::-1]
    else:
        return None
