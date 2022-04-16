class Weigthed_Graph:
    #入力定義
    def __init__(self, N=0, allow_multi=False, initialize=None, multi_edge=None):

        self.edge_number=0

        self.allow_multi=allow_multi
        self.initialize=initialize
        self.multi_edge=multi_edge

        self.adjacent=[{} for _ in range(N)]

    #頂点の追加
    def add_vertex(self):
        """ 頂点を追加する.

        """
        self.adjacent.append({})
        return self.order()-1

    def add_vertices(self, k):
        """ 頂点を k 個追加する.

        k: int
        """

        n=self.order()
        self.adjacent.extend([{} for _ in range(k)])
        return list(range(n,n+k))

    #辺の追加
    def add_edge(self, u, v, weight=1):
        """ 重さが weight の辺 uv を加える. """

        if self.allow_multi:
            self.edge_number+=1
            self.adjacent[u][v]=self.multi_edge(self.adjacent[u].get(v,self.initialize), weight)
            self.adjacent[v][u]=self.multi_edge(self.adjacent[v].get(u,self.initialize), weight)
        else:
            if not self.edge_exist(u,v):
                self.edge_number+=1
            self.adjacent[u][v]=weight
            self.adjacent[v][u]=weight

    #辺を除く
    def remove_edge(self,u,v):
        """ 辺 uv が存在するならば取り除く. """

        if self.edge_exist(u,v):
            del self.adjacent[u][v]
            del self.adjacent[v][u]
            self.edge_number-=1
            return  True
        else:
            return False

    #頂点を除く

    #Walkの追加

    #Cycleの追加

    #頂点の交換

    #グラフに辺が存在するか否か
    def edge_exist(self, u, v):
        """ 辺 uv が存在するかどうかを判定する. """

        return v in self.adjacent[u]

    #近傍
    def neighbohood(self,v):
        """ 頂点 v の近傍を返す. """
        return list(self.adjacent[v].keys())


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

    #距離

    #最短路

    #何かしらの頂点を選ぶ.

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
    N=G.vertex_count()
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
    N=G.vertex_count()
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
def Warshall_Floyd(G):
    """ Warshall–Floyd 法を用いて, 全点間距離を求める.

    G: 重み付き無向グラフ
    ※負の辺が存在する場合, -inf が発生する.
    """

    def three_loop():
        for u in range(N):
            Tu=T[u]
            for v in range(N):
                Tv=T[v]
                for w in range(N):
                    Tv[w]=min(Tv[w],Tv[u]+Tu[w])

    inf=float("inf"); N=G.vertex_count()

    T=[[0]*N for _ in range(N)]
    adj=G.adjacent
    for u in range(N):
        Tu=T[u]
        E=adj[u]
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
def Traveling_Salesman_Problem(G):
    N=G.vertex_count()

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

#木の直径を求める.
def Tree_Diameter(T, Mode=False):
    """ 重み付き木 T の直径を求める.

    T: 木

    (出力の結果)
    Mode=True  → (直径, (直径を成す端点1, 直径を成す端点2))
    Mode=False → 直径
    """
    from collections import deque

    def bfs(x):
        dist=[-1]*N; dist[x]=0
        adj=T.adjacent
        Q=deque([x])

        while Q:
            x=Q.popleft()
            for y,c in adj[x].items():
                if dist[y]==-1:
                    dist[y]=dist[x]+c
                    Q.append(y)

        z=max(range(N),key=lambda x:dist[x])
        return z,dist[z]

    N=T.vertex_count()
    u,_=bfs(0)
    v,d=bfs(u)

    if Mode:
        return (d,(u,v))
    else:
        return d

#最小全域木をクラシカル法で求める.
def Minimum_Spanning_Tree_by_Kruskal(G,Mode=0):
    """ グラフ G の最小全域木をクラシカル法で求める.

    G: グラフ
    Mode=0 → 重さのみ
    Mode=1 → 重さと使う辺
    Mode=2 → 重さと最小全域木
    """

    N=G.vertex_count()
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

    E=set()
    adj=G.adjacent
    for x in range(N):
        adj_x=adj[x]
        for y in adj_x:
            if x<y:
                E.add((x,y,adj_x[y]))
    E=sorted(E,key=lambda x:x[-1])

    W=0
    if Mode==1:
        F=[]
    elif Mode==2:
        T=Weigthed_Graph(N)

    count=N-1
    for x,y,w in E:
        if not same(x,y):
            count-=1
            union(x,y)
            W+=w

            if Mode==1:
                F.append((x,y))
            elif Mode==2:
                T.add_edge(x,y,w)

            if count==0:
                break

    if Mode==0:
        return W
    elif Mode==1:
        return W,F
    else:
        return W,T

def Minimum_Spanning_Tree_by_Prim(G,Mode=0):
    """ グラフ G の最小全域木をプリム法で求める.

    G: グラフ
    Mode=0 → 重さのみ
    Mode=1 → 重さと使う辺
    Mode=2 → 重さと最小全域木
    """
    from heapq import heapify,heappop,heappush
    N=G.vertex_count()

    S=[0]*N; S[0]=1
    H=[(w,0,y) for y,w in G.adjacent[0].items()]
    heapify(H)

    W=0
    if Mode==1:
        F=[]
    elif Mode==2:
        T=Weigthed_Graph(N)

    count=N-1
    while count:
        w,u,v=heappop(H)
        if S[u]==S[v]:
            continue

        count-=1
        W+=w

        if Mode==1:
            F.append((u,v))
        else:
            G.add_edge(u,v,w)

        if S[v]:
            u,v=v,u

        S[v]=1
        V=G.adjacent[v]
        for x in V:
            if not S[x]:
                heappush(H,(V[x],v,x))

    if Mode==0:
        return W
    elif Mode==1:
        return W,F
    else:
        return W,T
