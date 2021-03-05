class Digraph:
    """重み[なし]有向グラフを生成する.

    """

    #入力定義
    def __init__(self,vertex=[]):
        self.vertex=set(vertex)

        self.edge_number=0
        self.vertex_number=len(vertex)

        self.adjacent_out={v:set() for v in vertex} #出近傍(vが始点)
        self.adjacent_in={v:set() for v in vertex} #入近傍(vが終点)

    #頂点の追加
    def add_vertex(self,*adder):
        for v in adder:
            if not self.vertex_exist(v):
                self.adjacent_in[v]=set()
                self.adjacent_out[v]=set()

                self.vertex.add(v)
                self.vertex_number+=1

    #辺の追加
    def add_edge(self,From,To):
        self.add_vertex(From)
        self.add_vertex(To)

        if To not in self.adjacent_out[From]:
            self.adjacent_out[From].add(To)
            self.adjacent_in[To].add(From)
            self.edge_number+=1

    #辺を除く
    def remove_edge(self,From,To):
        self.add_vertex(From)
        self.add_vertex(To)

        if To in self.adjacent_out[From]:
            self.adjacent_out[From].discard(To)
            self.adjacent_in[To].discard(From)
            self.edge_number-=1

    #頂点を除く
    def remove_vertex(self,*vertexes):
        for  v in vertexes:
            if v in self.vertex:
                self.vertex_number-=1

                for u in self.adjacent_out[v]:
                    self.adjacent_in[u].discard(v)
                    self.edge_number-=1
                del self.adjacent_out[v]

                for u in self.adjacent_in[v]:
                    self.adjacent_out[u].discard(v)
                    self.edge_number-=1
                del self.adjacent_in[v]
                self.vertex.discard(v)

    #Walkの追加
    def add_walk(self,*walk):
        N=len(walk)
        for k in range(N-1):
            self.add_edge(walk[k],walk[k+1])

    #Cycleの追加
    def add_cycle(self,*cycle):
        self.add_walk(*cycle)
        self.add_edge(cycle[-1],cycle[0])

    #頂点の交換
    def __vertex_swap(self,p,q):
        self.vertex.sort()

    #グラフに頂点が存在するか否か
    def vertex_exist(self,v):
        return v in self.vertex

    #グラフに辺が存在するか否か
    def edge_exist(self,From,To):
        if self.vertex_exist(From) and self.vertex_exist(To):
            return False
        return To in self.adjacent_out[From]

    #近傍
    def neighbohood(self,v):
        """vの出近傍, 入近傍を出力する.

        Input:
        v:頂点

        Output:
        (出近傍, 入近傍)
        """
        if not self.vertex_exist(v):
            return (set(),set())
        return (self.adjacent_out[v],self.adjacent_in[v])

    #出次数
    def out_degree(self,v):
        if not self.vertex_exist(v):
            return 0
        return len(self.adjacent_out[v])

    #入次数
    def in_degree(self,v):
        if not self.vertex_exist(v):
            return 0
        return len(self.adjacent_in[v])

    #次数
    def degree(self,v):
        return (self.out_degree(v),self.in_degree(v))

    #頂点数
    def vertex_count(self):
        return self.vertex_number

    #辺数
    def edge_count(self):
        return self.edge_number

    #頂点vに到達可能な頂点
    def reachable_to(self,v):
        if not self.vertex_exist(v):
            return []

        from collections import deque
        T={v:0 for v in self.vertex}
        T[v]=1
        Q=deque([v])
        while Q:
            x=Q.popleft()
            for y in self.adjacent_in[x]:
                if not T[y]:
                    T[y]=1
                    Q.append(y)
        return [x for x in self.vertex if T[x]]

    #頂点vから到達可能な頂点
    def reachable_from(self,v):
        if not self.vertex_exist(v):
            return []

        from collections import deque
        T={v:0 for v in self.vertex}
        T[v]=1
        Q=deque([v])
        while Q:
            x=Q.popleft()
            for y in self.adjacent_out[x]:
                if not T[y]:
                    T[y]=1
                    Q.append(y)
        return [x for x in self.vertex if T[x]]

    #深いコピー
    def deepcopy(self):
        from copy import deepcopy
        D=Digraph()
        D.vertex=deepcopy(self.vertex)
        D.edge_number=self.edge_number
        D.vertex_number=len(self.vertex)
        D.adjacent_out=deepcopy(self.adjacent_out)
        D.adjacent_in=deepcopy(self.adjacent_in)
        return D

D=Digraph()
D.add_edge(1,3)
D.add_edge(2,3)
D.add_edge(3,4)
D.add_edge(3,5)
D.add_edge(4,6)
D.add_edge(6,1)
#================================================
#Dijkstra
def Dijkstra(D,From,To,with_path=False):
    """Dijksta法を用いて,FromからToまでの距離を求める.

    D:辺の重みが全て非負の有向グラフ
    From:始点
    To:終点
    with_path:最短路も含めて出力するか?

    (出力の結果)
    with_path=True->(距離,最短経路の辿る際の前の頂点)
    with_path=False->距離
    """
    from copy import copy
    from heapq import heappush,heappop

    T={v:float("inf") for v in D.vertex}
    T[From]=0

    if with_path:
        Prev={v:None for v in D.vertex}

    Q=[(0,From)]

    Flag=False
    while Q:
        c,u=heappop(Q)

        if u==To:
            Flag=True
            break

        if T[u]<c:
            continue

        for v in D.adjacent_out[u]:
            if T[v]>T[u]+1:
                T[v]=T[u]+1
                heappush(Q,(T[v],v))

                if with_path:
                    Prev[v]=u

    if not Flag:
        if with_path:
            return (float("inf"),None)
        else:
            return float("inf")

    if with_path:
        path=[To]
        u=To
        while (Prev[u]!=None):
            u=Prev[u]
            path.append(u)
        return (T[To],path[::-1])
    else:
        return T[To]

def Dijkstra_All(D,From,with_path=False):
    """Dijksta法を用いて,単一始点Fromからの距離を求める.

    D:辺の重みが全て非負の有向グラフ
    From:始点
    To:終点
    with_path:最短路も含めて出力するか?

    (出力の結果)
    with_path=True->(距離,最短経路の辿る際の前の頂点)
    with_path=False->距離
    """
    from copy import copy
    from heapq import heappush,heappop

    T={v:float("inf") for v in D.vertex}
    T[From]=0

    if with_path:
        Prev={v:None for v in D.vertex}

    Q=[(0,From)]

    while Q:
        c,u=heappop(Q)

        if T[u]<c:
            continue

        for v in D.adjacent_out[u]:
            if T[v]>T[u]+1:
                T[v]=T[u]+1
                heappush(Q,(T[v],v))

                if with_path:
                    Prev[v]=u

    if with_path:
        return (T,Prev)
    else:
        return  T

#Warshall–Floyd
def Warshall_Floyd(D):
    """Warshall–Floyd法を用いて,全点間距離を求める.

    D:負Cycleを含まない有向グラフ
    """
    T={v:{} for v in D.vertex} #T[u][v]:uからvへ
    for u in D.vertex:
        for v in D.vertex:
            if v==u:
                T[u][v]=0
            elif v in D.adjacent_out[u]:
                T[u][v]=1
            else:
                T[u][v]=float("inf")

    for u in D.vertex:
        for v in D.vertex:
            for w in D.vertex:
                T[v][w]=min(T[v][w],T[v][u]+T[u][w])

    return T

#FromからToへの(長さが丁度L or L以下の)Walkが存在するか否か
def walk_exist(graph,From,To,L,just=False):
    pass

#逆グラフの作成
def Inverse_Graph(D):
    """有向グラフDの全ての辺の向きを変えたグラフを出力する.

    D:有向グラフ
    """
    E=D.deepcopy()
    E.adjacent_out,E.adjacent_in=E.adjacent_in,E.adjacent_out
    return E

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

    X={v:D.in_degree(v) for v in D.vertex}
    Q=deque([v for v in D.vertex if X[v]==0])

    S=[]
    while Q:
        u=Q.pop()
        S.append(u)
        for v in D.adjacent_out[u]:
            X[v]-=1
            if X[v]==0:
                Q.append(v)
    return S

#DAG?
def Is_Directed_Acyclic_Graph(D):
    from collections import deque

    X={v:D.in_degree(v) for v in D.vertex}
    Q=deque([v for v in D.vertex if X[v]==0])
    S=0
    while Q:
        u=Q.pop()
        S+=1
        for v in D.adjacent_out[u]:
            X[v]-=1
            if X[v]==0:
                Q.append(v)
    return S==len(D.vertex)

#Cycleを縮約
def Cycle_Reduction(D):
    B,C=Strongly_Connected_Component_Decomposition(D,2)

    R=[K[0] for K in B]
    E=Digraph(R)
    for a in D.vertex:
        for b in D.adjacent_out[a]:
            if C[a]!=C[b]:
                E.add_edge(R[C[a]],R[C[b]])
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
    Group={v:0 for v in D.adjacent_out}
    Order=[]

    for v in D.adjacent_out:
        if Group[v]:continue

        S=[v]
        Group[v]=-1

        while S:
            u=S.pop()
            for w in D.adjacent_out[u]:
                if Group[w]:continue
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
            for w in D.adjacent_in[u]:
                if Group[w]!=-1:
                    continue

                Group[w]=k
                S.append(w)
        k+=1

    if Mode==0 or Mode==2:
        T=[[] for _ in range(k)]
        for v in D.adjacent_out:
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
    X=Strongly_Connected_Component_Decomposition(D)
    return len(X)

#誘導グラフ
def Induced_Subgraph(D,S):
    """D の頂点の部分集合 S から誘導される部分グラフ D[S] を出力する.

    D: 有向グラフ
    S: 頂点集合
    """
    S=set(S)
    E=D.deepcopy()

    R=[x for x in D.vertex if x not in S]
    for x in R:
        E.remove_vertex(x)
    return E

#Cycleが存在する?
def Is_Exist_Cycle(D):
    return not Is_Directed_Acyclic_Graph(D)

#Cycleを見つける.
#参考元:https://judge.yosupo.jp/submission/23992
def Find_Cycle(D):
    from collections import deque
    in_deg={v:len(D.adjacent_in[v]) for v in D.vertex}
    Q=deque([v for v in D.vertex if in_deg[v]==0])

    while Q:
        v=Q.popleft()
        for w in D.adjacent_out[v]:
            in_deg[w]-=1
            if in_deg[w]==0:
                Q.append(w)

    for v in D.vertex:
        P=[]
        if in_deg[v]==0:
            continue

        Q=deque([v])
        prev={x:None for x in D.vertex}
        while Q:
            x=Q.popleft()
            for y in D.adjacent_out[x]:
                if y==v:
                    prev[v]=x
                    break
                if prev[y] is not None:
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
def Depth_First_Search(G,prefunc=None,postfunc=None):
    """深さ優先探索を行う.

    G:グラフ
    prefunc:頂点をStackに入れる時,その頂点vに対して実行する関数,命令.
    postfunc:頂点をStackから出す時,その頂点vに対して実行する関数,命令.
    """
    from collections import deque
    T={v:False for v in G.vertex}
    v=G.vertex[0]

    S=deque([v])
    T[v]=True
    while S:
        v=S.pop()
        if postfunc:
            postfunc(v)

        for u in G.adjacent[v]:
            if not T[u]:
                T[u]=True
                S.append(u)
                if prefunc:
                    prefunc(u)

def Breath_First_Search(G,prefunc=None,postfunc=None):
    """幅優先探索を行う.

    G:グラフ
    prefunc:頂点をQueueに入れる時,その頂点vに対して実行する関数,命令.
    postfunc:頂点をQueueから出す時,その頂点vに対して実行する関数,命令.
    """
    from collections import deque
    T={v:False for v in G.vertex}
    v=G.vertex[0]

    Q=deque([v])
    T[v]=True
    while Q:
        v=Q.popleft()
        if postfunc:
            postfunc(v)

        for u in G.adjacent[v]:
            if not T[u]:
                T[u]=True
                Q.append(u)
                if prefunc:
                    prefunc(u)
