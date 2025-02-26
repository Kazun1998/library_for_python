class Weigthed_Digraph:
    #入力定義
    def __init__(self, N: int = 0, arc_offset: int = 0):
        """ N 頂点の重み付き有向グラフを生成する.

        Args:
            N (int, optional): 頂点数. Defaults to 0.
            arc_offset (int, optional): 弧番号の offset. Defaults to 0.
        """

        self.adjacent_out = [[] for _ in range(N)] # 出近傍 (v が始点)
        self.adjacent_in = [[] for _ in range(N)] # 入近傍 (v が終点)
        self.__size = 0
        self.__arc_offset = arc_offset

    # property

    # 頂点数
    @property
    def vertex_count(self) -> int:
        """ グラフの頂点数 (位数) を求める."""
        return len(self.adjacent_out)

    @property
    def order(self) -> int:
        """ グラフの位数 (頂点数) を求める."""
        return len(self.adjacent_out)

    #辺数
    @property
    def arc_count(self) -> int:
        """ グラフの辺数 (サイズ) を求める."""
        return self.__size

    @property
    def size(self) -> int:
        """ グラフのサイズ (辺数) を求める. """
        return self.__size

    #頂点の追加
    def add_vertex(self) -> int:
        """ 頂点を 1 個追加して, その頂点の番号を返す.

        Returns:
            int: 追加した頂点の番号
        """

        self.adjacent_out.append([])
        self.adjacent_in.append([])
        return self.order - 1

    def add_vertices(self, k: int) -> list[int]:
        """ 頂点を k 個追加して, その頂点の番号を返す.

        Returns:
            list[int]: 追加した k 個の頂点の番号のリスト
        """

        return [self.add_vertex() for _ in range(k)]

    #辺の追加
    def add_arc(self, source: int, target: int, weight: int = 1) -> int:
        """ source から target へ結ぶ重み weight の弧を追加し, 弧の番号を出力する.

        Args:
            source (int): 始点
            target (int): 終点
            weight (int, optional): 重み. Defaults to 1.

        Returns:
            int: 追加した弧の番号
        """

        id = self.arc_count + self.__arc_offset
        self.adjacent_out[source].append((target, weight, id))
        self.adjacent_in[target].append((source, weight, id))
        self.__size += 1
        return id

    #近傍

    #出次数
    def out_degree(self, v: int) -> int:
        """ 頂点 v の出次数 (v を始点とする有向辺の数) を求める

        Args:
            v (int): 頂点

        Returns:
            int: 出次数
        """

        return len(self.adjacent_out[v])

    #入次数
    def in_degree(self, v: int) -> int:
        """ 頂点 v の入次数 (v を終点とする有向辺の数) を求める

        Args:
            v (int): 頂点

        Returns:
            int: 入次数
        """
        return len(self.adjacent_in[v])

    #次数
    def degree(self, v: int) -> tuple[int, int]:
        """ 頂点 v について, タプル (出次数, 入次数) を求める

        Args:
            v (int): 頂点

        Returns:
            tuple[int, int]: (出次数, 入次数)
        """

        return (len(self.adjacent_out[v]), len(self.adjacent_in[v]))

    #相対次数
    def relative_degree(self, v: int) -> int:
        """ 頂点 v について, (出次数) - (入次数) を求める

        Args:
            v (int): 頂点

        Returns:
            int: (出次数) - (入次数)
        """

        return len(self.adjacent_out[v]) - len(self.adjacent_in[v])

#================================================
#Dijkstra
def Dijkstra_All(D, start, with_path=False):
    """ Dijksta 法を用いて, 単一始点 start からの距離を求める.

    D: 辺の重みが全て非負の有向グラフ
    start: 始点, to: 終点
    with_path: 最短路も含めて出力するか?

    (出力の結果)
    with_path=True → (距離, 最短経路の辿る際の前の頂点)
    with_path=False → 距離
    """
    from heapq import heappush,heappop

    inf=float("inf")
    N=D.vertex_count
    T=[inf]*N; T[start]=0

    if with_path:
        prev=[None]*N
        prev[start]=start

    adj_out=D.adjacent_out
    Q=[(0, start)]
    while Q:
        c,u=heappop(Q)
        if T[u]<c:
            continue

        E=adj_out[u]
        for v in E:
            if T[v]>c+E[v]:
                T[v]=c+E[v]
                heappush(Q,(T[v],v))

                if with_path:
                    prev[v]=u

    if with_path:
        return (T,prev)
    else:
        return  T

#Bellman_Ford
def Bellman_Ford_All(D, start):
    """ Bellman_Ford 法を用いて, 単一始点 start からの距離を求める (返り値が -inf になる場合がある).

    D: 有向グラフ
    start: 始点
    """

    inf=float("inf")
    N=D.vertex_count
    T=[inf]*N; T[start]=0

    adj_out=D.adjacent_out
    E=[]
    for u in range(N):
        F=adj_out[u]
        for v,cost in F.items():
            E.append((u,v,cost))

    for k in range(N):
        update=0
        for u,v,c in E:
            if T[v]>T[u]+c:
                T[v]=T[u]+c
                update=1
        if update==0:
            return T

    for _ in range(N):
        update=0
        for u,v,c in E:
            if T[v]>T[u]+c:
                T[v]=-inf
                update=1
        if update==0:
            break
    return T

#FromからToへの(長さが丁度L or L以下の)Walkが存在するか否か
def walk_exist(graph,From,To,L,just=False):
    pass

#逆グラフの作成
def Inverse_Graph(D):
    """有向グラフDの全ての辺の向きを変えたグラフを出力する.

    D:有向グラフ
    """
    from copy import deepcopy

    F=Weigthed_Digraph(D.vertex)

    F.arc_number=D.arc_number
    F.vertex_number=D.vertex_number

    F.adjacent_in=deepcopy(D.adjacent_out)
    F.adjacent_out=deepcopy(D.adjacent_in)
    return F

#補グラフの作成
def Complement_Graph(G):
    pass

#n頂点のランダムグラフ
def Random_Graph(n,p=0.5,seed=None):
    pass

#連結グラフ?
def Is_Connected(G):
    pass

#Topologycal Sort
def Topological_Sort(D):
    from collections import deque

    N=D.vertex_count
    X=[D.in_degree(x) for x in range(N)]
    Q=deque([v for v in range(N) if X[v]==0])

    adj_out=D.adjacent_out
    S=[]
    while Q:
        u=Q.pop()
        S.append(u)
        for v in adj_out[u]:
            X[v]-=1
            if X[v]==0:
                Q.append(v)

    if len(S)==N:
        return S
    else:
        return None

#DAG?
def Is_Directed_Acyclic_Graph(D):
    from collections import deque

    N=D.vertex_count
    X=[D.in_degree(x) for x in range(N)]
    Q=deque([v for v in range(N) if X[v]==0])

    S=0
    while Q:
        u=Q.pop()
        S+=1
        for v in D.adjacent_out[u]:
            X[v]-=1
            if X[v]==0:
                Q.append(v)

    return S==N

#Cycleを縮約
def Cycle_Reduction(D):
    pass

#強連結成分に分解
def Strongly_Connected_Component_Decomposition(D,Mode=0):
    """有向グラフDを強連結成分に分解

    Mode:
    0(Defalt)---各強連結成分の頂点のリスト
    1        ---各頂点が属している強連結成分の番号
    2        ---0,1の両方

    ※0で帰ってくるリストは各強連結成分に関してトポロジカルソートである.
    """
    N=D.vertex_count
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

#Cycleが存在する?
def Is_Exist_Cycle(D):
    return not Is_Directed_Acyclic_Graph(D)

#2部グラフ?
def Is_Bipartite_Graph(G):
    pass

#2部グラフの部集合に分割
def Bipartite_Separate(G):
    pass

#オイラーグラフ?
def Is_Eulerian_Graph(G):
    pass

#純オイラーグラフ?
def Is_Semi_Eulerian_Graph(G):
    pass

#Euler道を見つける
def Find_Eulerian_Trail(G):
    pass

#Euler閉路を見つける
def Find_Eulerian_Cycle(G):
    pass

#ハミルトングラフ?
def Is_Hamiltonian_Graph(G):
    pass

#ハミルトンを探す.
def Find_Hamiltonian_Graph(G):
    pass
