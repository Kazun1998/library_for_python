class Graph:
    __slots__=("edge_number", "adjacent")

    #入力定義
    def __init__(self, N=0):
        """ N 頂点の空グラフ (多重辺なし) を生成する."""

        self.edge_number=0
        self.adjacent=[set() for _ in range(N)]

    #頂点の追加
    def add_vertex(self):
        """ 頂点を追加する.

        """
        self.adjacent.append(set())
        return self.order()-1

    def add_vertices(self, k):
        """ 頂点を k 個追加する.

        k: int
        """

        n=self.order()
        self.adjacent.extend([set() for _ in range(k)])
        return list(range(n,n+k))

    #辺の追加
    def add_edge(self,u,v):
        """ 無向辺 uv を加える"""

        if not self.edge_exist(u,v):
            self.adjacent[u].add(v)
            self.adjacent[v].add(u)
            self.edge_number+=1
            return self.edge_number-1
        else:
            return -1

    #辺を除く
    def remove_edge(self,u,v):
        """ 無向辺 uv が存在するならば除く"""

        if self.edge_exist(u,v):
            self.adjacent[u].discard(v)
            self.adjacent[v].discard(u)
            self.edge_number-=1
            return True
        else:
            return False

    def reset_vertex(self, u):
        """ 頂点 u に接続している辺を全て消す."""

        X=self.adjacent[u].copy()
        for v in X:
            self.remove_edge(u,v)

    #Walkの追加
    def add_walk(self,*walk):
        """ walk=(w[0],...,w[n-1]) に対して, n-1 本の辺 w[i]w[i+1] を加える."""
        n=len(walk)
        for i in range(n-1):
            self.add_edge(walk[i],walk[i+1])

    #Cycleの追加
    def add_cycle(self,*cycle):
        """ cycle=(c[0], ..., c[n-1]) を加える. """
        self.add_walk(*cycle)
        self.add_edge(cycle[-1],cycle[0])

    #グラフに辺が存在するか否か
    def edge_exist(self,u,v):
        """ 辺 uv が存在するか? """
        return v in self.adjacent[u]

    #近傍
    def neighbohood(self,v):
        """ 頂点 v  の近傍を求める. """
        return self.adjacent[v]

    #次数
    def degree(self,v):
        """ 頂点 v の次数を求める. """
        if v in self.adjacent[v]:
            return len(self.adjacent[v])+1
        else:
            return len(self.adjacent[v])

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

        return self.edge_number

    def size(self):
        """ サイズ (辺の本数) を出力する. """

        return self.edge_number

    #頂点vを含む連結成分
    def connected_component(self,v):
        """ 頂点 v を含む連結成分を出力する."""

        from collections import deque
        N=len(self.adjacent)
        T=[0]*N; T[v]=1
        Q=deque([v])
        while Q:
            u=Q.popleft()
            for w in self.adjacent[u]:
                if T[w]==0:
                    T[w]=1
                    Q.append(w)
        return [x for x in range(N) if T[x]]

    #距離
    def distance(self,u,v):
        """ 2頂点 u,v 間の距離を求める."""

        if u==v:
            return 0

        from collections import deque
        inf=float("inf")
        N=len(self.adjacent)
        T=[inf]*N; T[u]=0

        Q=deque([u])
        while Q:
            w=Q.popleft()
            for x in self.adjacent[w]:
                if T[x]==inf:
                    T[x]=T[w]+1
                    Q.append(x)
                    if x==v:
                        return T[x]
        return inf

    #ある1点からの距離
    def distance_all(self,u):
        """ 頂点 u からの距離を求める."""

        from collections import deque
        inf=float("inf")
        N=len(self.adjacent)
        T=[inf]*N; T[u]=0

        Q=deque([u])
        while Q:
            w=Q.popleft()
            for x in self.adjacent[w]:
                if T[x]==inf:
                    T[x]=T[w]+1
                    Q.append(x)
        return T

    #最短路
    def shortest_path(self,u,v):
        """ u から v への最短路を求める (存在しない場合は None). """

        if u==v:
            return [u]

        from collections import deque
        inf=float("inf")
        T=[-1]*len(self.adjacent)

        Q=deque([u]); T[u]=u
        while Q:
            w=Q.popleft()
            for x in self.adjacent[w]:
                if T[x]==-1:
                    T[x]=w
                    Q.append(x)
                    if x==v:
                        P=[v]
                        a=v
                        while a!=u:
                            a=T[a]
                            P.append(a)
                        return P[::-1]
        return None

    def edge_yielder(self):
        g=self.adjacent
        for v in range(self.vertex_count()):
            for w in g[v]:
                if v<=w:
                    yield (v,w)

    def pop_neighborhood(self, v):
        assert self.adjacent[v]
        w=self.adjacent[v].pop()
        self.adjacent[v].add(w)
        return w

#==========
#グラフの生成
#==========
#補グラフの作成
def Complement_Graph(G):
    """ グラフ G の補グラフを求める."""

    N=G.vertex_count(); V=set(range(N))
    H=Graph(N)

    for u in range(N):
        H.adjacent[u]=V-G.adjacent[u]-{u}
    return H

# N 頂点のランダムグラフ
def Random_Graph(N, p=0.5, self_loop=False, seed=None):
    import random
    G=Graph(N)

    random.seed(seed)
    for u in range(N):
        for v in range(u,N):
            if u==v and self_loop==False:
                continue

            if random.random()<p:
                G.add_edge(u,v)
    return G

def Directed_Sum(*G):
    offset=0
    H=Graph()
    for g in G:
        n=g.vertex_count()
        H.add_vertices(n)
        for i,j in g.edge_yielder():
            H.add_edge(i+offset, j+offset)
        offset+=n
    return H

#==========
#連結グラフ?
def Is_Connected(G):
    from collections import deque

    N=G.vertex_count()
    T=[0]*N; T[0]=1
    Q=deque([0])

    Q_popleft=Q.popleft
    Q_append=Q.append
    adj=G.adjacent

    while Q:
        u=Q_popleft()
        for v in adj[u]:
            if T[v]==0:
                T[v]=1
                Q_append(v)

    return all(T)

def Lowlink(G, mode=0):
    """ G の ord, lowlink を求める.

    G: Graph

    output: (ord, lowlink)
    """

    from collections import deque

    N=G.vertex_count()
    ord=[-1]*N; low=[-1]*N
    flag=[0]*N
    adj=G.adjacent
    parent=[-1]*N

    #BFSパート
    for v in range(N):
        if flag[v]:
            continue

        k=0
        S=deque([v])
        T=[]

        while S:
            u=S.pop()
            if flag[u]:
                continue

            T.append(u)
            ord[u]=k
            k+=1
            flag[u]=1

            for w in adj[u]:
                if not flag[w]:
                    S.append(w)
                    parent[w]=u

        for u in T:
            low[u]=ord[u]

        for w in T[:0:-1]:
            for x in adj[w]:
                if w==v or x!=parent[w]:
                    low[w]=min(low[w],low[x],ord[x])

    if mode==0:
        return ord, low
    else:
        return ord, low, parent

#橋列挙
def Bridge(G):
    """ G にある橋を列挙する.

    G: Graph
    """
    ord,low=Lowlink(G)
    return [(u,v) for u,v in G.edge_yielder() if ord[u]<low[v] or ord[v]<low[u]]

#関節点の列挙
def Articulation_Point(G):
    from collections import deque

    N=G.vertex_count()
    A=[]; A_append=A.append
    ord=[-1]*N; low=[-1]*N
    flag=[0]*N
    adj=G.adjacent

    parent=[-1]*N; children=[[] for _ in range(N)]

    #BFSパート
    for v in range(N):
        if flag[v]:
            continue

        k=0
        S=deque([v])
        T=[]
        X=[]

        while S:
            u=S.pop()
            if flag[u]:
                continue

            T.append(u)
            ord[u]=k
            k+=1
            flag[u]=1

            for w in adj[u]:
                if not flag[w]:
                    S.append(w)
                    parent[w]=u

        for w in T:
            low[w]=ord[w]

        for w in T[:0:-1]:
            children[parent[w]].append(w)

        for w in T[:0:-1]:
            for x in adj[w]:
                if w==v or x!=parent[w]:
                    low[w]=min(low[w],low[x],ord[x])

        #根での判定
        if len(children[v])>=2:
            A_append(v)

        #根以外の判定
        for w in T[:0:-1]:
            for u in children[w]:
                if ord[w]<=low[u]:
                    A_append(w)
                    break
    return A

#二辺連結成分分解
def Two_Edge_Connected_Components(G):
    """グラフ G を二辺連結成分分解 (橋を含まない) する.

    [input]
    G: Graph
    """

    N=G.vertex_count()

    ord,low=Lowlink(G)

    T=[0]*N; C=[]
    for v in range(N):
        if T[v]==1:
            continue

        T[v]=1
        Q=[v]; c=[]
        while Q:
            v=Q.pop()
            c.append(v)

            for w in G.adjacent[v]:
                if (ord[v]>=low[w] and ord[w]>=low[v]) and T[w]==0:
                    T[w]=1
                    Q.append(w)
        C.append(c)
    return C

#=====
#森?
def Is_Forest(G):
    """ 森かどうか判定する. """

    C=Connected_Component_Number(G)
    M=G.edge_count()
    return G.vertex_count()==M+C

#木?
def Is_Tree(G):
    """ 木かどうか判定する. """
    C=Connected_Component_Number(G)
    M=G.edge_count()
    return C==1 and G.vertex_count()==M+C

#木の直径
def Tree_Diameter(T,Mode=False):
    """ 木 T の直径を求める.

    T: 木

    (出力の結果)
    Mode=True → (直径, (直径を成す端点1, 直径を成す端点2))
    Mode=False → 直径
    """
    from collections import deque

    def __bfs(x):
        N=T.vertex_count()
        D=[-1]*N
        D[x]=0
        Q=deque([x])
        while Q:
            x=Q.popleft()

            for y in T.adjacent[x]:
                if D[y]==-1:
                    D[y]=D[x]+1
                    Q.append(y)
        z=max(range(N),key=lambda x:D[x])
        return z,D[z]

    u,_=__bfs(0)
    v,d=__bfs(u)

    if Mode:
        return (d,(u,v))
    else:
        return d

#連結成分に分解
def Connected_Component_Decomposition(G, mode=0):
    """ 連結成分毎に分解する.

    G: Graph
    mode:0 → 連結成分, 1 → 連結成分番号, 2 → (連結成分, 連結成分番号)"""
    from collections import deque

    N=G.vertex_count()
    T=[-1]*N
    C=[]
    k=0
    for v in range(N):
        if T[v]==-1:
            Q=deque([v]); T[v]=k
            c=[]
            while Q:
                u=Q.popleft()
                c.append(u)
                for w in G.adjacent[u]:
                    if T[w]==-1:
                        T[w]=k
                        Q.append(w)
            k+=1
            C.append(c)

    if mode==0:
        return C
    elif mode==1:
        return  T
    else:
        return C,T

#連結成分の個数
def Connected_Component_Number(G):
    """ 連結成分の個数を求める. """

    from collections import deque

    N=G.vertex_count()
    T=[0]*N
    K=0
    for v in range(N):
        if T[v]==0:
            Q=deque([v]);T[v]=1
            K+=1
            while Q:
                u=Q.popleft()
                for w in G.adjacent[u]:
                    if T[w]==0:
                        T[w]=1
                        Q.append(w)
    return K

#Cycleが存在する?
def Is_Exist_Cycle(G):
    from collections import deque

    N=G.vertex_count()
    T=[0]*N
    adj=G.adjacent

    for v in range(N):
        if not T[v]:
            x=v
            T[v]=1
            S=deque([v])
            while S:
                u=S.popleft()
                for w in adj[u]:
                    if T[w]==0:
                        T[w]=1
                        S.append(w)
                    elif x!=w:
                        return True
                x=u

    return False

#2部グラフ?
def Is_Bipartite_Graph(G):
    """ 2部グラフかどうかを判定する. """

    N=G.vertex_count()
    T=[0]*N
    adj=G.adjacent

    for v in range(N):
        if T[v]==0:
            T[v]=1
            S=[v]
            while S:
                u=S.pop()
                for w in adj[u]:
                    if T[w]==0:
                        T[w]=-T[u]
                        S.append(w)
                    elif T[w]==T[u]:
                        return False
    return True

#2部グラフの部集合に分割
def Bipartite_Separate(G):
    """ 2部グラフの頂点を部集合に分割する. """

    N=G.vertex_count()
    T=[0]*N
    adj=G.adjacent

    Bip=[]
    for v in range(N):
        if T[v]==0:
            T[v]=1
            S=[v]
            A=[]; B=[]
            while S:
                u=S.pop()

                if T[u]==1:
                    A.append(u)
                else:
                    B.append(u)

                for w in adj[u]:
                    if T[w]==0:
                        T[w]=-T[u]
                        S.append(w)
                    elif T[w]==T[u]:
                        return None
            Bip.append((A,B))

    return Bip

#オイラーグラフ?
def Is_Eulerian_Graph(G):
    """ グラフ G がオイラーグラフかどうかを判定する. """

    N=G.vertex_count()
    for v in range(N):
        if G.degree(v)%2:
            return False
    return Is_Connected(G)

#準オイラーグラフ?
def Is_Semi_Eulerian_Graph(G):
    """ グラフ G が準オイラーグラフかどうかを判定する. """

    K=0
    N=G.vertex_count()
    for v in range(N):
        if G.degree(v)%2:
            K+=1
            if K==3:
                return False
    return K==2 and Is_Connected(G)

#Euler 路を見つける
def Find_Eulerian_Trail(G):
    K=0
    N=G.vertex_count()
    for v in range(N-1,-1,-1):
        if G.degree(v)%2:
            K+=1
            start=v

            if K==3:
                return None
    if K==0:
        return None

    from copy import deepcopy
    E=deepcopy(G.adjacent)

    temp=[start]; v=start
    while E[v]:
        w=E[v].pop()
        E[w].remove(v)
        temp.append(w)
        v=w

    path=[]
    while temp:
        v=temp.pop()
        if E[v]:
            temp.append(v)
            while E[v]:
                w=E[v].pop()
                E[w].remove(v)
                temp.append(w)
                v=w
        else:
            path.append(v)

    path.reverse()
    return path if len(path)-1==G.size() else None

#Euler閉路を見つける
def Find_Eulerian_Cycle(G):
    N=G.vertex_count()
    for v in range(N):
        if G.degree(v)%2:
            return None

    from copy import deepcopy
    E=deepcopy(G.adjacent)

    temp=[0]; v=0
    while E[v]:
        w=E[v].pop()
        E[w].remove(v)
        temp.append(w)
        v=w

    cycle=[]
    while temp:
        v=temp.pop()
        if E[v]:
            temp.append(v)
            while E[v]:
                w=E[v].pop()
                E[w].remove(v)
                temp.append(w)
                v=w
        else:
            cycle.append(v)

    cycle.reverse()
    return cycle if len(cycle)-1==G.size() else None

#ハミルトングラフ?
def Is_Hamiltonian_Graph(G):
    """ ハミルトングラフ (全ての頂点を1回ずつ通るサイクルを含むグラフ) かどうかを判定する.

    """

    N=G.order()
    if N==2 or N==0:
        return False
    elif N==1:
        return True

    pass

#ハミルトンを探す.
def Find_Hamiltonian_Graph(G):
    from collections import deque

    N=G.order()
    if N==2 or N==0:
        return None
    elif N==1:
        return [0]

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

    X=unit
    while True:
        A=[]
        for u in range(N):
            if V[u] and deg[u]<M_sqrt:
                for v in range(N):
                    if u!=v and V[v] and G.edge_exist(u,v):
                        A.append(v)
                A.append(u)
                break

        if not A:
            break

        K=len(A)-1
        bit=[0]*K
        for i in range(K):
            for j in range(i):
                if not G.edge_exist(A[i],A[j]):
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
            if A[-1]!=v and V[v] and G.edge_exist(A[-1],v):
                deg[v]-=1

    A=[]
    for u in range(N):
        if V[u]:
            A.append(u)

    K=len(A)
    bit=[0]*K
    for i in range(K):
        for j in range(i):
            if not G.edge_exist(A[i], A[j]):
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

    deg=G.degree; adj=G.adjacent
    for i in range(N):
        for j in adj[i]:
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

#---------------------------------------
def One_Point_Distance(G,From,with_path=False):
    """ 単一始点 From からの距離を求める.

    G: グラフ
    From: 始点
    with_path: 最短路も含めて出力するか?

    (出力の結果)
    with_path=True → (距離, 最短経路の辿る際の前の頂点)
    with_path=False → 距離
    """

    from collections import deque

    N=G.vertex_count(); adj=G.adjacent
    inf=float("inf")
    T=[inf]*N; T[From]=0

    if with_path:
        Prev=[None]*N

    Q=deque([From])

    while Q:
        u=Q.popleft()

        for v in adj[u]:
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
def Warshall_Floyd(G):
    """ Warshall-Floyd 法を用いて, 全点間距離を求める.

    """

    N=G.vertex_count(); inf=float("inf"); adj=G.adjacent
    T=[[0]*N for _ in range(N)]

    for u in range(N):
        Tu=T[u]
        for v in range(N):
            if v==u:
                T[u][v]=0
            elif v in adj[u]:
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

print(Is_Hamiltonian_Graph(Complete_Graph(12)))
