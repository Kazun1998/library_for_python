class Weigthed_Graph:
    #入力定義
    def __init__(self,vertex=[]):
        self.vertex=set(vertex)

        self.edge_number=0
        self.adjacent={v:{} for v in vertex}

    #頂点の追加
    def add_vertex(self,*adder):
        for v in adder:
            if not self.vertex_exist(v):
                self.adjacent[v]={}
                self.vertex.add(v)

    #辺の追加
    def add_edge(self,u,v,Weight):
        self.add_vertex(u)
        self.add_vertex(v)

        if not self.edge_exist(u,v):
            self.edge_number+=1

        self.adjacent[u][v]=Weight
        self.adjacent[v][u]=Weight

    #辺を除く
    def remove_edge(self,u,v):
        self.add_vertex(u)
        self.add_vertex(v)

        if self.edge_exist(u,v):
            del self.adjacent[u][v]
            del self.adjacent[v][u]
            self.edge_number-=1

    #頂点を除く
    def remove_vertex(self,*vertexes):
        for v in vertexes:
            if self.vertex_exist(v):
                U=self.neighbohood(v)
                for u in self.adjacent[v]:
                    del self.adjacent[u][v]
                    self.edge_number-=1
                del self.adjacent[v]

    #Walkの追加

    #Cycleの追加

    #頂点の交換

    #グラフに頂点が存在するか否か
    def vertex_exist(self,v):
        return v in self.vertex

    #グラフに辺が存在するか否か
    def edge_exist(self,u,v):
        if not (self.vertex_exist(u) and self.vertex_exist(v)):
            return False
        return v in self.adjacent[u]

    #近傍
    def neighbohood(self,v):
        if not self.vertex_exist(v):
            return []
        return list(self.adjacent[v].keys())


    #頂点数
    def vertex_count(self):
        return len(self.adjacent)

    #辺数

    #頂点vを含む連結成分

    #距離

    #最短路

    #何かしらの頂点を選ぶ.
    def poping_vertex(self):
        v=self.vertex.pop()
        self.vertex.add(v)
        return v

#Dijkstra
def Dijkstra(G,From,To,with_path=False):
    """Dijksta法を用いて,FromからToまでの距離を求める.

    G:辺の重みが全て非負の無向グラフ
    From:始点
    To:終点
    with_path:最短路も含めて出力するか?

    (出力の結果)
    with_path=True->(距離,最短経路の辿る際の前の頂点)
    with_path=False->距離
    """
    from heapq import heappush,heappop

    inf=float("inf")
    T={v:inf for v in G.adjacent}
    T[From]=0

    if with_path:
        Prev={v:None for v in G.adjacent}

    Q=[(0,From)]

    Flag=False
    while Q:
        c,u=heappop(Q)

        if u==To:
            Flag=True
            break

        if T[u]<c:
            continue

        E=G.adjacent[u]
        for v in E:
            p=T[u]+E[v]
            if T[v]>p:
                T[v]=p
                heappush(Q,(p,v))

                if with_path:
                    Prev[v]=u

    if not Flag:
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

def Dijkstra_All(G,From,with_path=False):
    """Dijksta法を用いて,Fromから各頂点までの距離を求める.

    G:辺の重みが全て非負の無向グラフ
    From:始点
    with_path:最短路も含めて出力するか?

    (出力の結果)
    with_path=True->(距離,最短経路の辿る際の前の頂点)
    with_path=False->距離
    """
    from heapq import heappush,heappop

    inf=float("inf")
    T={v:inf for v in G.adjacent}
    T[From]=0

    if with_path:
        Prev={v:None for v in G.adjacent}

    Q=[(0,From)]

    while Q:
        c,u=heappop(Q)

        if T[u]<c:
            continue

        E=G.adjacent[u]
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
    """Warshall–Floyd法を用いて,全点間距離を求める.

    D:負Cycleを含まない有向グラフ
    """
    T={v:{} for v in G.adjacent} #T[u][v]:uからvへ

    inf=float("inf")
    for u in G.adjacent:
        for v in G.adjacent:
            if v==u:
                T[u][v]=0
            elif v in G.adjacent[u]:
                T[u][v]=G.adjacent[u][v]
            else:
                T[u][v]=inf

    for u in G.adjacent:
        E=T[u]
        for v in G.adjacent:
            F=T[v]
            for w in G.adjacent:
                F[w]=min(F[w],F[u]+E[w])

    return T

#巡回セールスマン問題を解く.
def Traveling_Salesman_Problem(D):
    N=len(D.vertex)
    I=list(D.vertex)

    inf=float("inf")
    T=[[inf]*N for _ in range(1<<N)]
    T[0][0]=0

    for S in range(1<<N):
        F=T[S]
        for v in range(N):
            if S&(1<<v):
                continue

            E=T[S|1<<v]
            Dist=D.adjacent[I[v]]

            for w in range(N):
                if v!=w and E[v]>F[w]+Dist[I[w]]:
                    E[v]=F[w]+Dist[I[w]]
    return T[-1][0]

#木の直径を求める.
def Tree_Diameter(T,Mode=False):
    """重み付き木Tの直径を求める.

    T:木

    (出力の結果)
    Mode=True->(直径,(直径を成す端点1,直径を成す端点2))
    Mode=False->直径
    """
    from collections import deque

    def bfs(x):
        D={y:-1 for y in T.adjacent}
        D[x]=0
        Q=deque([x])
        while Q:
            x=Q.popleft()

            for y,c in T.adjacent[x].items():
                if D[y]==-1:
                    D[y]=D[x]+c
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

#最小全域木をクラシカル法で求める.
def Minimum_Spanning_Tree_by_Kruskal(G,Mode=0):
    """グラフGの最小全域木をクラシカル法で求める.

    G:グラフ
    Mode=0→重さのみ, 1→重さと使う辺, 2→重さと最小全域木
    """
    #Union-Findを定義する.
    U={x:x for x in G.vertex}
    R={x:1 for x in G.vertex}

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
    for x in G.vertex:
        X=G.adjacent[x]
        for y in X:
            if (y,x,X[y]) not in E:
                E.add((x,y,X[y]))
    E=sorted(E,key=lambda x:x[-1])[::-1]

    W=0
    if Mode==1:
        F=[]
    elif Mode==2:
        T=Weigthed_Graph(G.vertex)

    count=len(G.vertex)-1
    while count:
        x,y,w=E.pop()
        if not same(x,y):
            count-=1
            union(x,y)
            W+=w

            if Mode==1:
                F.append((x,y))
            elif Mode==2:
                T.add_edge(x,y,w)

    if Mode==0:
        return W
    elif Mode==1:
        return W,F
    else:
        return W,T

def Minimum_Spanning_Tree_by_Prim(G,Mode=0):
    """グラフGの最小全域木をプリム法で求める.

    G:グラフ
    Mode=0→重さのみ, 1→重さと使う辺, 2→重さと最小全域木
    """
    from heapq import heapify,heappop,heappush

    start=G.poping_vertex()
    S={x:0 for x in G.vertex}
    S[start]=1
    H=[(w,start,y) for y,w in G.adjacent[start].items()]
    heapify(H)

    W=0
    if Mode==1:
        F=[]
    elif Mode==2:
        T=Weigthed_Graph(G.vertex)

    count=len(G.vertex)-1
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

H=Weigthed_Graph([1,2,3,4,5,6,7])
E=[(1,2,2),(1,3,3),(1,4,5),(2,4,7),(3,5,2),(4,5,15),(4,6,1),(5,7,11),(6,7,8)]

for x,y,w in E:
    H.add_edge(x,y,w)
