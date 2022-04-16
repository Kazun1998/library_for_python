class Weigthed_Digraph:
    """重み[付き]有向グラフを生成する.

    """
    #入力定義
    def __init__(self, N=0, allow_multi=False, multi_edge=None, initialize=None):
        """ 重み[付き]有向グラフを生成する.

        N: 頂点数
        allow_multi: 多重辺を認めるか?
        multi_edge: 多重辺における重みのまとめ方 (重みに関する2変数関数)
        initilize: multi_edge の単位元
        """

        self.arc_number=0

        self.allow_multi=allow_multi
        self.initialize=initialize
        self.multi_edge=multi_edge

        self.adjacent_out=[{} for _ in range(N)] #出近傍(vが始点)
        self.adjacent_in=[{} for _ in range(N)] #入近傍(vが終点)

    #頂点の追加
    def add_vertex(self):
        """ 頂点を追加する.

        """
        self.adjacent_out.append({})
        self.adjacent_in.append({})
        return self.order()-1

    def add_vertices(self, k):
        """ 頂点を k 個追加する.

        k: int
        """

        n=self.order()
        self.adjacent_out.extend([{} for _ in range(k)])
        self.adjacent_in.extend([{} for _ in range(k)])
        return list(range(n,n+k))

    #辺の追加(更新)
    def add_arc(self, source, target, weight=1):
        if self.allow_multi:
            self.arc_number+=1
            self.adjacent_out[source][target]=self.multi_edge(self.adjacent_out[source].get(target, self.initialize), weight)
            self.adjacent_in[target][source]=self.multi_edge(self.adjacent_in[source].get(target, self.initialize), weight)
        else:
            if target not in self.adjacent_out[source]:
                self.arc_number+=1
            self.adjacent_out[source][target]=weight
            self.adjacent_in[target][source]=weight

    #辺を除く
    def remove_arc(self, source, target):
        if self.arc_exist(source, target):
            self.arc_number-=1
            del self.adjacent_out[source][target]
            del self.adjacent_in[target][source]
            return True
        else:
            return False

    #頂点を除く
    def remove_vertex(self,*vertexes):
        pass

    #Walkの追加
    def add_walk(self,*walk):
        pass

    #Cycleの追加
    def add_cycle(self,*cycle):
        pass

    #頂点の交換
    def __vertex_swap(self,p,q):
        pass

    #グラフに辺が存在するか否か
    def arc_exist(self, source, target):
        return target in self.adjacent_out[source]

    #近傍
    def neighbohood(self,v):
        """vの出近傍, 入近傍を出力する.

        Input:
        v:頂点

        Output:
        (出近傍, 入近傍)
        """

        return (set(self.adjacent_out[v].keys()),set(self.adjacent_in[v].keys()))

    #出次数
    def out_degree(self,v):
        return len(self.adjacent_out[v])

    #入次数
    def in_degree(self,v):
        return len(self.adjacent_in[v])

    #次数
    def degree(self,v):
        return (self.out_degree(v),self.in_degree(v))

    #相対次数
    def relative_degree(self, v):
        return self.out_degree(v)-self.in_degree(v)

    #頂点数
    def vertex_count(self):
        """ グラフの頂点数 (位数) を求める."""
        return len(self.adjacent_out)

    def order(self):
        """ グラフの位数 (頂点数) を求める."""
        return len(self.adjacent_out)

    #辺数
    def arc_count(self):
        """ グラフの辺数 (サイズ) を求める."""
        return self.arc_number

    def size(self):
        """ グラフのサイズ (辺数) を求める. """
        return self.arc_number

    #頂点vに到達可能な頂点
    def reachable_to(self,v):
        from collections import deque

        N=self.vertex_count()
        adj_in=self.adjacent_in

        T=[0]*N; T[v]=1
        Q=deque([v])
        while Q:
            x=Q.popleft()
            for y in adj_in[x]:
                if not T[y]:
                    T[y]=1
                    Q.append(y)
        return [x for x in range(N) if T[x]]

    #頂点vから到達可能な頂点
    def reachable_from(self,v):
        from collections import deque

        N=self.vertex_count()
        adj_out=self.adjacent_out

        T=[0]*N; T[v]=1
        Q=deque([v])
        while Q:
            x=Q.popleft()
            for y in adj_out[x]:
                if not T[y]:
                    T[y]=1
                    Q.append(y)
        return [x for x in range(N) if T[x]]

    #深いコピー
    def deepcopy(self):
        from copy import deepcopy
        D=Weigthed_Digraph(self.vertex_count())
        D.arc_number=self.arc_count()
        D.adjacent_out=deepcopy(self.adjacent_out)
        D.adjacent_in=deepcopy(self.adjacent_in)
        return D
#================================================
#Dijkstra
def Dijkstra(D, start , goal, with_path=False):
    """ Dijksta 法を用いて, start から goal までの距離を求める.

    D: "辺の重みが全て非負" の有向グラフ
    start: 始点, goal: 終点
    with_path: 最短路も含めて出力するか?

    (出力の結果)
    with_path=True → (距離, 最短経路)
    with_path=False → 距離
    """

    from heapq import heappush,heappop

    inf=float("inf")
    N=D.vertex_count()
    T=[inf]*N; T[start]=0

    if with_path:
        prev=[None]*N
        prev[start]=start

    Q=[(0, start)]

    adj_out=D.adjacent_out
    flag=0
    while Q:
        c,u=heappop(Q)

        if u==goal:
            flag=1
            break

        if T[u]<c:
            continue

        E=adj_out[u]
        for v in E:
            p=T[u]+E[v]
            if T[v]>p:
                T[v]=p
                heappush(Q,(p,v))

                if with_path:
                    prev[v]=u

    if not flag:
        if with_path:
            return (inf,[])
        else:
            return inf

    if with_path:
        path=[goal]
        u=goal
        while u!=start:
            u=prev[u]
            path.append(u)
        return (T[goal],path[::-1])
    else:
        return T[goal]

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
    N=D.vertex_count()
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
def Bellman_Ford(D, start, goal):
    """ Bellman_Ford 法を用いて, start から goal までの距離を求める (返り値が -inf になる場合がある).

    D:有向グラフ
    start: 始点, goal: 終点
    """

    inf=float("inf")
    N=D.vertex_count()
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
            return T[goal]

    for _ in range(N):
        update=0
        for u,v,c in E:
            if T[v]>T[u]+c:
                T[v]=-inf
                update=1
        if update==0:
            break
    return T[goal]

def Bellman_Ford_All(D, start):
    """ Bellman_Ford 法を用いて, 単一始点 start からの距離を求める (返り値が -inf になる場合がある).

    D: 有向グラフ
    start: 始点
    """

    inf=float("inf")
    N=D.vertex_count()
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

#Warshall–Floyd
def Warshall_Floyd(D):
    """ Warshall–Floyd 法を用いて, 全点間距離を求める.

    D: 重み付き有向グラフ
    """

    def three_loop():
        for u in range(N):
            Tu=T[u]
            for v in range(N):
                Tv=T[v]
                for w in range(N):
                    Tv[w]=min(Tv[w],Tv[u]+Tu[w])

    inf=float("inf"); N=D.vertex_count()

    T=[[0]*N for _ in range(N)]
    adj_out=D.adjacent_out
    for u in range(N):
        Tu=T[u]
        E=adj_out[u]
        for v in range(N):
            if v==u:
                Tu[v]=0
            elif v in E:
                Tu[v]=E[v]
            else:
                Tu[v]=inf

    three_loop()

    flag=1
    for v in range(N):
        if T[v][v]<0:
            T[v][v]=-inf
            flag=0

    if flag==1:
        return T
    else:
        three_loop()
        return T

#巡回セールスマン問題を解く.
def Traveling_Salesman_Problem(D):
    """ 巡回セールスマン問題を解く. """

    N=D.vertex_count()

    inf=float("inf")
    T=[[inf]*N for _ in range(1<<N)]
    T[0][0]=0

    for S in range(1<<N):
        F=T[S]
        for v in range(N):
            if S&(1<<v):
                continue

            E=T[S|1<<v]
            cost=D.adjacent_out[v]

            for w in cost:
                if v!=w and E[v]>F[w]+cost[w]:
                    E[v]=F[w]+cost[w]
    return T[-1][0]

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

    N=D.vertex_count()
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

    N=D.vertex_count()
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
#-------------------------------------------------
#特別なグラフ
#-------------------------------------------------
#完全グラフの作成
def Complete_Graph(n):
    pass

#完全2部グラフ
def Complete_Bipartite_Graph(m,n):
    pass

#グラフ作成
def Making_Graph(V,E):
    pass

#空グラフの作成
def Empty_Graph(n):
    pass

#ペテルセングラフ
def Petersen_Graph(n=5,k=2):
    pass

#格子グラフ
def Grid_Graph(m,n):
    pass

#Pathグラフ
def Path_Graph(n):
    pass

#Cycleグラフ
def Cycle_Graph(n):
    pass

#Starグラフ
def Star_Graph(n):
    pass

#Wheelグラフ
def Wheel_Graph(n):
    pass

#騎士巡回グラフ
def Knight_Tour_Graph(m,n):
    pass

#完全k分木
def Complete_Kary_Tree(n,k=2):
    pass

#---------------------------------------
#グラフの捜査
#---------------------------------------
def Depth_First_Search(D, start, prefunc=None, postfunc=None):
    """深さ優先探索を行う.

    D: グラフ
    prefunc: 頂点をStackに入れる時,その頂点vに対して実行する関数,命令.
    postfunc: 頂点をStackから出す時,その頂点vに対して実行する関数,命令.
    """
    from collections import deque

    N=D.vertex_count()
    T=[0]*N; T[start]=1
    adj_out=D.adjacent_out

    S=deque([start])

    if prefunc:
        prefunc(start)

    while S:
        v=S.pop()
        if postfunc:
            postfunc(v)

        for u in adj_out[v]:
            if T[u]==0:
                T[u]=1
                S.append(u)
                if prefunc:
                    prefunc(u)

def Breath_First_Search(D, start, prefunc=None, postfunc=None):
    """幅優先探索を行う.

    D: グラフ
    prefunc: 頂点をQueueに入れる時,その頂点vに対して実行する関数,命令.
    postfunc: 頂点をQueueから出す時,その頂点vに対して実行する関数,命令.
    """
    from collections import deque

    N=D.vertex_count()
    T=[0]*N; T[start]=1
    adj_out=D.adjacent_out

    Q=deque([start])

    if prefunc:
        prefunc(start)

    while Q:
        v=Q.popleft()
        if postfunc:
            postfunc(v)

        for u in adj_out[v]:
            if T[u]==0:
                T[u]=1
                Q.append(u)
                if prefunc:
                    prefunc(u)
