class Graph:
    #入力定義
    def __init__(self,N):
        """ N 頂点の空グラフ (多重辺なし) を生成する."""

        self.N=N
        self.edge_number=0
        self.adjacent=[set() for _ in range(N)]

    #辺の追加
    def add_edge(self,u,v):
        """ 無向辺 uv を加える"""

        if not self.edge_exist(u,v):
            self.adjacent[u].add(v)
            self.adjacent[v].add(u)
            self.edge_number+=1

    #辺を除く
    def remove_edge(self,u,v):
        """ 無向辺 uv が存在するならば除く"""

        if self.edge_exist(u,v):
            self.adjacent[u].discard(v)
            self.adjacent[v].discard(u)
            self.edge_number-=1

    #Walkの追加
    def add_walk(self,*walk):
        """ walk=(w[0],...,w[n-1]) に対して, n-1 本の辺 w[i]w[i+1] を加える."""
        n=len(walk)
        for i in range(n-1):
            self.add_edge(walk[i],walk[i+1])

    #Cycleの追加
    def add_cycle(self,*cycle):
        self.add_walk(*cycle)
        self.add_edge(cycle[-1],cycle[0])

    #グラフに辺が存在するか否か
    def edge_exist(self,u,v):
        return v in self.adjacent[u]

    #近傍
    def neighbohood(self,v):
        return self.adjacent[v]

    #次数
    def degree(self,v):
        if v in self.adjacent[v]:
            return len(self.adjacent[v])+1
        else:
            return len(self.adjacent[v])

    #頂点数
    def vertex_count(self):
        return self.N

    #辺数
    def edge_count(self):
        """ 辺の本数を出力する."""

        return self.edge_number

    #頂点vを含む連結成分
    def connected_component(self,v):
        """ 頂点 v を含む連結成分を出力する."""

        from collections import deque
        T=[0]*self.N; T[v]=1
        Q=deque([v])
        while Q:
            u=Q.popleft()
            for w in self.adjacent[u]:
                if T[w]==0:
                    T[w]=1
                    Q.append(w)
        return [x for x in range(self.N) if T[x]]

    #距離
    def distance(self,u,v):
        """ 2頂点 u,v 間の距離を求める."""

        if u==v:
            return 0

        from collections import deque
        inf=float("inf")
        T=[inf]*self.N; T[u]=0

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
        T=[inf]*self.N; T[u]=0

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
        T=[-1]*self.N

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

#補グラフの作成
def Complement_Graph(G):
    """ グラフ G の補グラフを求める."""

    N=G.N; V=set(range(N))
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

#連結グラフ?
def Is_Connected(G):
    from collections import deque

    N=G.N
    T=[0]*N; T[0]=1
    Q=deque([0])

    Q_popleft=Q.popleft
    Q_append=Q.append
    adj=G.adjacent
    K=0

    while Q:
        u=Q_popleft()
        K+=1
        for v in adj[u]:
            if T[v]==0:
                T[v]=1
                Q_append(v)

    return K==N

#橋列挙
def Bridge(G):
    from collections import deque

    N=G.N
    B=[]
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
        X=[]

        while S:
            u=S.pop()
            if flag[u]:
                continue

            T.append(u)
            ord[u]=k
            k+=1
            flag[u]=1

            if u!=v:
                X.append((parent[u],u))

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

        for u,w in X:
            if ord[u]<low[w]:
                if u>w:
                    u,w=w,u
                B.append((u,w))
    return B

#関節点の列挙
def Articulation_Point(G):
    from collections import deque

    N=G.N
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
    from collections import defaultdict

    N=G.N

    #Union-Findを定義する.
    U=list(range(N))
    R=[1]*N

    def find(x):
        if U[x]==x:
            return x

        A=[x]
        while x!=U[x]:
            x=U[x]
            A.append(x)

        for a in A:
            U[a]=x
        return x

    def union(x,y):
        x=find(x)
        y=find(y)

        if x==y:
            return

        if R[x]>R[y]:
            U[y]=x
        else:
            U[x]=y
            if R[x]==R[y]:
                R[y]+=1

    def same(x,y):
        return find(x)==find(y)

    Taboo=[set() for _ in range(N)]
    for u,v in Bridge(G):
        Taboo[u].add(v)
        Taboo[v].add(u)

    adj=G.adjacent
    for u in range(N):
        for v in adj[u]:
            if v not in Taboo[u]:
                union(u,v)

    D=defaultdict(list)
    for v in range(N):
        D[find(v)].append(v)
    return list(D.values())

#=====
#森?
def Is_Forest(G):
    """ 森かどうか判定する. """

    C=Connected_Component_Number(G)
    M=G.edge_count()
    return G.N==M+C

#木?
def Is_Tree(G):
    """ 木かどうか判定する. """
    C=Connected_Component_Number(G)
    M=G.edge_count()
    return C==1 and G.N==M+C

#木の直径
def Tree_Diameter(T,Mode=False):
    """ 木 T の直径を求める.

    T: 木

    (出力の結果)
    Mode=True → (直径, (直径を成す端点1, 直径を成す端点2))
    Mode=False → 直径
    """
    from collections import deque

    def bfs(x):
        D={y:-1 for y in T.adjacent}
        D[x]=0
        Q=deque([x])
        while Q:
            x=Q.popleft()

            for y in T.adjacent[x]:
                if D[y]==-1:
                    D[y]=D[x]+1
                    Q.append(y)

        z=max(D,key=lambda x:D[x])
        return z,D[z]

    for x in T.adjacent:
        break

    u,_=bfs(x)
    v,d=bfs(u)

    if Mode:
        return (d,(u,v))
    else:
        return d

#連結成分に分解
def Connected_Component_Decomposition(G):
    """ 連結成分毎に分解する. """

    T=[0]*G.N
    C=[]
    for v in range(G.N):
        if T[v]==0:
            X=G.connected_component(v)
            for x in X:
                T[x]=1
            C.append(X)
    return C

#連結成分の個数
def Connected_Component_Number(G):
    """ 連結成分の個数を求める. """

    T=[0]*G.N
    C=0
    for v in range(G.N):
        if T[v]==0:
            X=G.connected_component(v)
            for x in X:
                T[x]=1
            C+=1
    return C

#Cycleが存在する?
def Is_Exist_Cycle(G):
    from collections import deque
    T=[0]*G.N
    adj=G.adjacent

    for v in G.vertex:
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

    from collections import deque
    T=[0]*G.N
    adj=G.adjacent

    for v in range(G.N):
        if T[v]==0:
            T[v]=1
            S=deque([v])
            while S:
                u=S.popleft()
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

    from collections import deque
    T=[0]*G.N
    adj=G.adjacent

    for v in range(G.N):
        if T[v]==0:
            T[v]=1
            S=deque([v])
            while S:
                u=S.popleft()
                for w in adj[u]:
                    if T[w]==0:
                        T[w]=-T[u]
                        S.append(w)
                    elif T[w]==T[u]:
                        return None, None

    U=[u for u in range(G.N) if T[u]==1]
    V=[v for v in range(G.N) if T[v]==-1]
    return U,V

#オイラーグラフ?
def Is_Eulerian_Graph(G):
    """ グラフ G がオイラーグラフかどうかを判定する. """

    for v in range(G.N):
        if G.degree(v)%2:
            return False
    return Is_Connected(G)

#準オイラーグラフ?
def Is_Semi_Eulerian_Graph(G):
    """ グラフ G が準オイラーグラフかどうかを判定する. """

    K=0
    for v in range(G.N):
        if G.degree(v)%2:
            K+=1
            if K==3:
                return False
    return K==2 and Is_Connected(G)

#Euler 路を見つける
def Find_Eulerian_Trail(G):
    K=0
    for v in range(G.N-1,-1,-1):
        if G.degree(v)%2:
            K+=1
            s=v

            if K==3:
                return None
    if K==0:
        return None

    from copy import deepcopy
    E=deepcopy(G.adjacent)

    def dfs(w):
        X=[w]
        while E[w]:
            u=E[w].pop()
            E[u].discard(w)
            X.append(u)
            w=u
        return X

    P=sum([dfs(v) for v in dfs(s)],[])

    if len(P)-1==G.edge_count():
        return P
    else:
        return None

#Euler閉路を見つける
def Find_Eulerian_Cycle(G):
    for v in range(G.N-1,-1,-1):
        if G.degree(v)%2:
            return None

    from copy import deepcopy
    E=deepcopy(G.adjacent)

    def dfs(w):
        X=[w]
        while E[w]:
            u=E[w].pop()
            E[u].discard(w)
            X.append(u)
            w=u
        return X

    P=sum([dfs(v) for v in dfs(0)],[])

    if len(P)-1==G.edge_count():
        return P
    else:
        return None

#ハミルトングラフ?
def Is_Hamiltonian_Graph(G):
    N=len(G.vertex)
    if N==2 or N==0:
        return False
    elif N==1:
        return True

    A=G.vertex[0]
    B=G.vertex[1]
    C=G.vertex[2]

    X={v:False for v in G.vertex}
    X[A]=True
    #------------------------------
    def __f__(v,k):
        if k==0:
            return v in G.adjacent[A]

        if v==B and X[C]:
            return False

        for w in G.adjacent[v]:
            if not X[w]:
                X[w]=True
                if __f__(w,k-1):
                    return True
                X[w]=False

        return False
    #------------------------------
    return __f__(A,N-1)

#ハミルトンを探す.
def Find_Hamiltonian_Graph(G):
    from collections import deque

    N=len(G.vertex)
    if N==2 or N==0:
        return None
    elif N==1:
        return G.vertex

    A=G.vertex[0]
    B=G.vertex[1]
    C=G.vertex[2]

    X={v:False for v in G.vertex}
    X[A]=True
    Y=deque([A])
    #------------------------------
    def __f__(v,k):
        if k==0:
            return v in G.adjacent[A]

        if v==B and X[C]:
            return False

        for w in G.adjacent[v]:
            if not X[w]:
                X[w]=True
                Y.append(w)
                if __f__(w,k-1):
                    return True
                X[w]=False
                _=Y.pop()

        return False
    #------------------------------
    if __f__(A,N-1):
        return list(Y)
    else:
        return None

#-------------------------------------------------
#特別なグラフ
#-------------------------------------------------
#完全グラフの作成
def Complete_Graph(N):
    """ N 頂点の完全グラフを生成する. """

    G=Graph(N)
    V=set(range(N))
    for u in range(N):
        G.adjacent[u]=V-{u}
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
    for i in range(N-1):
        C.add_edge(i,i+1)
    C.add_edge(N-1,0)
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

    N=G.N; adj=G.adjacent
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
    """ Warshall–Floyd 法を用いて, 全点間距離を求める.

    """

    N=G.N; inf=float("inf"); adj=G.adjacent
    T=[[0]*N for _ in range(N)]

    for u in range(N):
        for v in range(N):
            Tu=T[u]
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
#---------------------------------------
#グラフの捜査
#---------------------------------------
def Depth_First_Search(G,start=0,prefunc=None,postfunc=None):
    """深さ優先探索を行う.

    G:グラフ
    prefunc:頂点をStackに入れる時,その頂点vに対して実行する関数,命令.
    postfunc:頂点をStackから出す時,その頂点vに対して実行する関数,命令.
    """

    from collections import deque

    N=G.N; adj=G.adjacent
    T=[0]*N; T[start]=1

    S=deque([start])

    if prefunc:
        prefunc(start)

    while S:
        v=S.pop()
        if postfunc:
            postfunc(v)

        for u in adj[v]:
            if not T[u]:
                T[u]=1
                S.append(u)
                if prefunc:
                    prefunc(u)

def Breath_First_Search(G,start=0,prefunc=None,postfunc=None):
    """幅優先探索を行う.

    G:グラフ
    prefunc:頂点をQueueに入れる時,その頂点vに対して実行する関数,命令.
    postfunc:頂点をQueueから出す時,その頂点vに対して実行する関数,命令.
    """

    from collections import deque

    N=G.N; adj=G.adjacent
    T=[0]*N; T[start]=1

    Q=deque([start])

    if prefunc:
        prefunc(start)

    while Q:
        v=Q.popleft()
        if postfunc:
            postfunc(v)

        for u in adj[v]:
            if not T[u]:
                T[u]=1
                Q.append(u)
                if prefunc:
                    prefunc(u)
