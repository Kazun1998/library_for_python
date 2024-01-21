class Digraph:
    """重み[なし]有向グラフを生成する.

    """

    #入力定義
    def __init__(self, N=0):
        """ N 頂点の空グラフを生成する. """


        self.arc_number=0
        self.adjacent_out=[set() for v in range(N)]#出近傍(vが始点)
        self.adjacent_in=[set() for v in range(N)] #入近傍(vが終点)

    #頂点の追加
    def add_vertex(self):
        """ 頂点を追加する.

        """
        self.adjacent_out.append(set())
        self.adjacent_in.append(set())
        return self.order()-1

    def add_vertices(self, k=1):
        """ 頂点を k 個追加する.

        k: int
        """
        n=self.order()
        self.adjacent_out.extend([set() for _ in range(k)])
        self.adjacent_in.extend([set() for _ in range(k)])
        return list(range(n,n+k))

    #辺の追加
    def add_arc(self, source, target, mode=0):
        if target not in self.adjacent_out[source]:
            self.adjacent_out[source].add(target)
            self.adjacent_in[target].add(source)
            self.arc_number+=1
            if mode:
                return self.arc_number-1
        else:
            if mode:
                return -1
    #辺を除く
    def remove_arc(self, source, target):
        if target in self.adjacent_out[source]:
            self.adjacent_out[source].discard(target)
            self.adjacent_in[target].discard(source)
            self.arc_number-=1

    def reset_vertex(self, u):
        """ 頂点 u に接続している辺を全て消す."""

        X=self.adjacent_out[u].copy()
        for v in X:
            self.remove_arc(u,v)

        X=self.adjacent_in[u].copy()
        for w in X:
            self.remove_arc(w,u)


    #Walkの追加
    def add_walk(self,*walk):
        """ 有向歩道 walk=(w[0], ..., w[n-1]) を追加する. """

        N=len(walk)
        for k in range(N-1):
            self.add_arc(walk[k],walk[k+1])

    #Cycleの追加
    def add_cycle(self,*cycle):
        """ 有向サイクル cycle=(c[0] ..., c[n-1]) を追加する. """

        self.add_walk(*cycle)
        self.add_arc(cycle[-1],cycle[0])

    #グラフに辺が存在するか否か
    def arc_exist(self, u, v):
        """ 有向辺 u -> v は存在するか? """
        return (v in self.adjacent_out[u])

    #近傍
    def neighbohood(self,v):
        """vの出近傍, 入近傍を出力する.

        Input:
        v:頂点

        Output:
        (出近傍, 入近傍)
        """
        return (self.adjacent_out[v],self.adjacent_in[v])

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
    def relative_degree(self,v):
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
        """ 頂点 v に到達可能な頂点を求める. """
        from collections import deque

        N=self.vertex_count()
        T=[0]*N; T[v]=1
        Q=deque([v])
        while Q:
            x=Q.pop()
            for y in self.adjacent_in[x]:
                if not T[y]:
                    T[y]=1
                    Q.append(y)
        return [x for x in range(N) if T[x]]

    #頂点vから到達可能な頂点
    def reachable_from(self,v):
        """ 頂点 v へ到達可能な頂点を求める. """
        from collections import deque

        N=self.vertex_count()
        T=[0]*N; T[v]=1
        Q=deque([v])
        while Q:
            x=Q.pop()
            for y in self.adjacent_out[x]:
                if not T[y]:
                    T[y]=1
                    Q.append(y)
        return [x for x in range(N) if T[x]]

    #頂点 u,v の距離を求める.
    def distance(self, u, v, default = -1):
        from collections import deque

        adj_out = self.adjacent_out
        dist = [-1] * self.vertex_count()
        dist[u] = 0

        Q=deque([u])
        while Q:
            x = Q.popleft()
            for y in adj_out[x]:
                if dist[y] != -1:
                    continue

                dist[y] = dist[x] + 1
                Q.append(y)

                if y == v:
                    return dist[y]

        return default

    #ある1点からの距離
    def distance_all(self, u, default):
        """ 頂点 u からの距離をそれぞれの頂点について求める."""

        from collections import deque

        adj_out = self.adjacent_out
        dist = [-1] * self.vertex_count()
        dist[u] = 0

        Q=deque([u])
        while Q:
            x = Q.popleft()
            for y in adj_out[x]:
                if dist[y] != -1:
                    continue

                dist[y] = dist[x]+1
                Q.append(y)

        return [d if d != -1 else default for d in dist]

    def shortest_path(self,u,v, dist=False):
        """ u から v への最短路を求める (存在しない場合は None).

        dist: False → shortest_path のみ, True → (dist, shortest_path)"""

        if u==v:
            if dist:
                return (0,[u])
            else:
                return [u]

        from collections import deque
        inf=float("inf")

        adj_in=self.adjacent_in
        T=[-1]*self.vertex_count()

        Q=deque([v]); T[v]=v
        while Q:
            w=Q.popleft()
            for x in adj_in[w]:
                if T[x]==-1:
                    T[x]=w
                    Q.append(x)
                    if x==u:
                        P=[u]
                        a=u
                        while a!=v:
                            a=T[a]
                            P.append(a)
                        if dist:
                            return (len(P)-1,P)
                        else:
                            return P
        if dist:
            return (inf,None)
        else:
            return None

    #深いコピー
    def deepcopy(self):
        from copy import deepcopy
        D=Digraph(self.vertex_count())
        D.arc_number=self.arc_count()
        D.adjacent_out=deepcopy(self.adjacent_out)
        D.adjacent_in=deepcopy(self.adjacent_in)
        return D

#================================================
#Dijkstra
def One_Point_Distance(D, From, with_path=False):
    """ 単一始点 From からの距離を求める.

    D: 辺の重みが全て非負の有向グラフ
    From:始点
    with_path:最短路も含めて出力するか?

    (出力の結果)
    with_path=True → (距離, 最短経路の辿る際の前の頂点)
    with_path=False → 距離
    """

    N=D.vertex_count(); inf=float("inf"); adj_out=D.adjacent_out
    T=[inf]*N; T[From]=0

    if with_path:
        Prev=[None]*N

    from collections import deque
    Q=deque([From])
    while Q:
        u=Q.popleft()

        for v in D.adjacent_out[u]:
            if T[v]==inf:
                T[v]=T[u]+1
                Q.append(v)

                if with_path:
                    Prev[v]=u

    if with_path:
        return (T,Prev)
    else:
        return  T

#Warshall–Floyd
def Warshall_Floyd(D):
    """Warshall–Floyd法を用いて,全点間距離を求める.

    D: 有向グラフ
    """

    N=D.vertex_count(); inf=float("inf"); adj_out=D.adjacent_out
    T=[[0]*N for _ in range(N)]

    for u in range(N):
        for v in range(N):
            Tu=T[u]
            if v==u:
                T[u][v]=0
            elif v in adj_out[u]:
                T[u][v]=1
            else:
                T[u][v]=float("inf")

    for u in range(N):
        Tu=T[u]
        for v in range(N):
            Tv=T[v]
            for w in range(N):
                Tv[w]=min(Tv[w],Tv[u]+Tu[w])

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

#2部グラフ?
def Is_Bipartite_Graph(G):
    pass

#2部グラフの部集合に分割
def Bipartite_Separate(G):
    pass

#オイラーグラフ?
def Is_Eulerian_Graph(D):
    pass

#準オイラーグラフ?
def Is_Semi_Eulerian_Graph(D):
    pass

#Euler道を見つける
def Find_Eulerian_Trail(D):
    N=D.vertex_count()
    s=-1
    for v in range(N):
        k=D.relative_degree(v)
        if abs(k)>=2:
            return None
        elif k==1:
            if s>=0:
                return None
            s=v
    if s==-1:
        return None

    from copy import deepcopy
    A=deepcopy(D.adjacent_out)

    def dfs(w):
        X=[w]
        while A[w]:
            u=A[w].pop()
            A[u].discard(w)
            X.append(u)
            w=u
        return X

    P=[]
    Q=dfs(s)
    while Q:
        u=Q.pop()
        P.append(u)
        if len(A[u])>0:
            Q.extend(dfs(u)[:-1])

    if len(P)-1==D.arc_count():
        return P[::-1]
    else:
        return None

#Euler閉路を見つける
def Find_Eulerian_Cycle(D):
    N=D.vertex_count()
    for v in range(N):
        if D.relative_degree(v):
            return None

    from copy import deepcopy
    A=deepcopy(D.adjacent_out)
    def dfs(w):
        X=[w]
        while A[w]:
            u=A[w].pop()
            A[u].discard(w)
            X.append(u)
            w=u
        return X

    P=[]
    Q=dfs(0)
    while Q:
        u=Q.pop()
        P.append(u)
        if len(A[u])>0:
            Q.extend(dfs(u)[:-1])

    if len(P)-1==D.arc_count():
        return P[::-1]
    else:
        return None

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
def Making_Digraph(N, A):
    D=Digraph(N)
    for a in A:
        D.add_arc(*a)
    return D

#空グラフの作成
def Empty_Graph(N):
    return Digraph(N)

#ペテルセングラフ
def Petersen_Graph(n=5,k=2):
    pass

#格子グラフ
def Grid_Graph(m,n):
    pass

#Pathグラフ
def Directed_Path_Graph(N):
    """ N 頂点の有向サイクルを生成する. """

    P=Digraph(N)
    for i in range(N-1):
        P.add_arc(i,i+1)
    return P

#Cycleグラフ
def Directed_Cycle_Graph(N, reverse=False):
    """ N 頂点の有向サイクルを生成する. """

    C=Digraph(N)
    for i in range(N):
        if reverse:
            j=(i-1)%N
        else:
            j=(i+1)%N
        C.add_arc(i,j)
    return C

#Circulant グラフ
def Circulant_Graph(N, *J):
    """ N 頂点, J ジャンプの巡回グラフを生成する."""

    C=Digraph(N)
    for j in J:
        for v in range(N):
            w=(v+j)%N
            C.add_arc(v,w)
    return C

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

    D: 有向グラフ
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
    """ 幅優先探索を行う.

    D: 有向グラフ
    prefunc: 頂点をStackに入れる時,その頂点vに対して実行する関数,命令.
    postfunc: 頂点をStackから出す時,その頂点vに対して実行する関数,命令.
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
