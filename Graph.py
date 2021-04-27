<<<<<<< HEAD
class Graph:
    #入力定義
    def __init__(self,vertex=[]):
        self.vertex=set(vertex)

        self.edge_number=0
        self.adjacent={v:set() for v in vertex}

    #頂点の追加
    def add_vertex(self,*adder):
        for v in adder:
            if not self.vertex_exist(v):
                self.adjacent[v]=set()
                self.vertex.add(v)

    #辺の追加
    def add_edge(self,u,v):
        self.add_vertex(u)
        self.add_vertex(v)

        if not self.edge_exist(u,v):
            self.adjacent[u].add(v)
            self.adjacent[v].add(u)
            self.edge_number+=1

    #辺を除く
    def remove_edge(self,u,v):
        self.add_vertex(u)
        self.add_vertex(v)

        if self.edge_exist(u,v):
            self.adjacent[u].discard(v)
            self.adjacent[v].discard(u)
            self.edge_number-=1

    #頂点を除く
    def remove_vertex(self,*vertexes):
        for v in vertexes:
            if self.vertex_exist(v):
                U=self.neighbohood(v)
                for u in U:
                    self.edge_number-=1
                    self.adjacent[u].discard(v)

                del self.adjacent[v]
                self.vertex.discard(v)

    #Walkの追加
    def add_walk(self,*walk):
        n=len(walk)
        for i in range(n-1):
            self.add_edge(walk[i],walk[i+1])

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
    def edge_exist(self,u,v):
        if not(self.vertex_exist(u) and self.vertex_exist(v)):
            return False
        return v in self.adjacent[u]

    #近傍
    def neighbohood(self,v):
        if not self.vertex_exist(v):
            return []
        return list(self.adjacent[v])

    #次数
    def degree(self,v):
        if not self.vertex_exist(v):
            return 0

        return len(self.adjacent[v])

    #頂点数
    def vertex_count(self):
        return len(self.vertex)

    #辺数
    def edge_count(self):
        return self.edge_number

    #頂点vを含む連結成分
    def connected_component(self,v):
        if v not in self.adjacent:
            return []

        from collections import deque
        T={u:0 for u in self.vertex}
        T[v]=1
        Q=deque([v])
        while Q:
            u=Q.popleft()
            for w in self.adjacent[u]:
                if not T[w]:
                    T[w]=1
                    Q.append(w)
        return [x for x in self.adjacent if T[x]]

    #距離
    def distance(self,u,v):
        from collections import deque
        inf=float("inf")
        T={v:inf  for v in self.vertex}

        if u==v:
            return 0
        Q=deque([u])
        T[u]=0
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
        from collections import deque
        inf=float("inf")
        T={v:inf  for v in self.vertex}

        Q=deque([u])
        T[u]=0
        while Q:
            w=Q.popleft()
            for x in self.adjacent[w]:
                if T[x]==inf:
                    T[x]=T[w]+1
                    Q.append(x)
        return T

    #最短路
    def shortest_path(self,u,v):
        from collections import deque
        inf=float("inf")
        T={v:None for v in self.vertex}

        if u==v:
            return [u]

        Q=deque([u])
        T[u]=u
        while Q:
            w=Q.popleft()
            for x in self.adjacent[w]:
                if not T[x]:
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

    #何かしらの頂点を選ぶ.
    def poping_vertex(self):
        v=self.vertex.pop()
        self.vertex.add(v)
        return v

#FromからToへの(長さが丁度L or L以下の)Walkが存在するか否か
def walk_exist(graph,From,To,L,just=False):
    if L<0:
        return False
    if From==To and just==False:
        return True
    if From==To and just==True and L==0:
        return True

    F=False
    for w in graph.neighbohood(From):
        if graph.edge_exist(From,w):
            F=F or walk_exist(graph,w,To,L-1,just=just)
    return F

#補グラフの作成
def Complement_Graph(G):
    import copy
    n=len(G.vertex)
    H=Graph(copy.deepcopy(G.vertex))
    for j in range(n):
        for i in range(j+1,n):
            if G.adjacent[j][i]==0:
                H.add_edge(G.vertex[i],G.vertex[j])
    return H

#n頂点のランダムグラフ
def Random_Graph(n,p=0.5,seed=None):
    import random
    G=Empty_Graph(n)
    if p<0:p=0
    elif p>1:p=1

    random.seed(seed)
    for j in range(1,n+1):
        for i in range(j+1,n+1):
            if random.random()<p:
                G.add_edge(i,j)
    return G

#連結グラフ?
def Is_Connected(G):
    from collections import deque
    T={u:False for u in G.vertex}
    v=G.poping_vertex()

    Q=deque([v])
    Q_popleft=Q.popleft
    Q_append=Q.append
    K=0
    while Q:
        u=Q_popleft()
        for w in G.adjacent[u]:
            if not T[w]:
                T[w]=True
                Q_append(w)
                K+=1

    return (K==G.vertex_count())

V=[0,1,2,3,4,5,6,7,8]
E=[(0,1),(1,2),(0,4),(1,5),(2,6),(3,4),(4,5),(5,6),(6,7),(4,8)]
G=Graph(V)

for x,y in E:
    G.add_edge(x,y)

#橋列挙
def Bridge(G):
    from collections import deque

    B=[]
    ord={v:-1 for v in G.vertex}
    flag={v:0 for v in G.vertex}
    nei=G.adjacent

    #BFSパート
    for v in G.vertex:
        if flag[v]:
            continue

        k=0
        parent={}
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

            for w in nei[u]:
                if not flag[w]:
                    S.append(w)
                    parent[w]=u

        low={v:ord[v] for v in T}
        for w in T[:0:-1]:
            for x in nei[w]:
                if w==v or x!=parent[w]:
                    low[w]=min(low[w],low[x],ord[x])

        for u,w in X:
            if ord[u]<low[w]:
                B.append((u,w))
    return B

#関節点の列挙
def Articulation_Point(G):
    from collections import deque

    A=[];A_append=A.append
    ord={v:-1 for v in G.vertex}
    flag={v:0 for v in G.vertex}
    nei=G.adjacent

    #BFSパート
    for v in G.vertex:
        if flag[v]:
            continue

        k=0
        parent={}
        children={}
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

            for w in nei[u]:
                if not flag[w]:
                    S.append(w)
                    parent[w]=u

        children={v:[] for v in T}
        for w in T[:0:-1]:
            children[parent[w]].append(w)

        low={v:ord[v] for v in T}
        for w in T[:0:-1]:
            for x in nei[w]:
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

    Taboo={v:set() for v in G.vertex}
    for u,v in Bridge(G):
        Taboo[u].add(v)
        Taboo[v].add(u)

    nei=G.adjacent
    for u in G.vertex:
        for v in nei[u]:
            if v not in Taboo[u]:
                union(u,v)

    D=defaultdict(list)
    for v in G.vertex:
        D[find(v)].append(v)
    return list(D.values())

#木?
def Is_Tree(G):
    if G.edge_count()!=len(G.vertex)-1:
        return False
    return Is_Connected(G)

#木の直径
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
    T={v:False for v in G.vertex}
    C=[]
    for v in G.vertex:
        if not T[v]:
            X=G.connected_component(v)
            for x in X:
                T[x]=True
            C.append(X)
    return C

#連結成分の個数
def Connected_Component_Number(G):
    T={v:False for v in G.vertex}
    C=0
    for v in G.vertex:
        if not T[v]:
            X=G.connected_component(v)
            for x in X:
                T[x]=True
            C+=1
    return C

#Cycleが存在する?
def Is_Exist_Cycle(G):
    from collections import deque
    T={u:False for u in G.vertex}

    for v in G.vertex:
        if not T[v]:
            x=v
            T[v]=True
            S=deque([v])
            while S:
                u=S.popleft()
                for w in G.neighbohood(u):
                    if not T[w]:
                        T[w]=True
                        S.append(w)
                    elif x!=w:
                        return True
                x=u

    return False

#2部グラフ?
def Is_Bipartite_Graph(G):
    from collections import deque
    T={u:0 for u in G.vertex}

    for v in G.vertex:
        if not T[v]:
            x=v
            T[v]=1
            S=deque([v])
            while S:
                u=S.popleft()
                for w in G.adjacent[u]:
                    if T[w]==0:
                        T[w]=-T[u]
                        S.append(w)
                    elif T[w]==T[u]:
                        return False
                x=u

    return True

#2部グラフの部集合に分割
def Bipartite_Separate(G):
    from collections import deque
    T={u:0 for u in G.vertex}

    for v in G.vertex:
        if not T[v]:
            x=v
            T[v]=1
            S=deque([v])
            while S:
                u=S.popleft()
                for w in G.adjacent[u]:
                    if T[w]==0:
                        T[w]=-T[u]
                        S.append(w)
                    elif T[w]==T[u]:
                        return None
                x=u

    U=[u for u in G.vertex if T[u]==1]
    V=[v for v in G.vertex if T[v]==-1]
    return U,V

#オイラーグラフ?
def Is_Eulerian_Graph(G):
    for v in G.vertex:
        if G.degree(v)%2:
            return False
    return True

#純オイラーグラフ?
def Is_Semi_Eulerian_Graph(G):
    K=0
    for v in G.vertex:
        if G.degree(v)%2:
            K+=1
            if K==3:
                return False
    return K==2

#純オイラーグラフ?
def Find_Eulerian_Trail(G):
    U=[]
    K=0
    for v in G.vertex:
        if G.degree(v)%2:
            K+=1
            U.append(v)

            if K==3:
                return False

#Euler閉路を見つける
def Find_Eulerian_Cycle(G):
    from copy import deepcopy

    if not Is_Eulerian_Graph(G):
        return None

    N=len(G.vertex)
    K=G.vertex_count()
    A=deepcopy(G.adjacent)

    U,V=G.vertex[0],G.vertex[-1]
    X=U
    P=[U]

    while X!=V:
        X=G.neighbohood(X)[0]
        P.append(X)

    print(P)

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
def Complete_Graph(n):
    G=Graph([i+1 for i in range(n)])
    for v in range(1,n+1):
        for u in range(v+1,n+1):
            G.add_edge(u,v)
    return G

#完全2部グラフ
def Complete_Bipartite_Graph(m,n):
    X=list(range(-1,-(m+1),-1))+list(range(1,n+1))
    G=Graph(X)

    for x in range(1,m+1):
        for y in range(1,n+1):
            G.add_edge(-x,y)

    return G

#グラフ作成
def Making_Graph(V,E):
    S=set(V)
    for e in E:
        try:
            if len(e)!=2:
                return None
        except:
            return None
        a,b=e

    G=Graph(V)

    for e in E:
        G.add_edge(*e)
    return G

#空グラフの作成
def Empty_Graph(n):
    return Graph(list(range(1,n+1)))

#ペテルセングラフ
def Petersen_Graph(n=5,k=2):
    V=list(range(1,n+1))+list(range(-1,-(n+1),-1))

    G=Graph(V)
    for i in range(n):
        G.add_edge(i+1,-(i+1))
        G.add_edge(i+1,(i+1)%n+1)
        G.add_edge(-(i+1),-((i+k)%n+1))
    return G

#格子グラフ
def Grid_Graph(m,n):
    """m x n マスのグラフを生成する.
    """
    E=[]
    for x in range(1,m+1):
        E+=[(x,y) for y in range(1,n+1)]

    G=Graph(E)
    H=[(1,0),(0,1)]

    for y in range(1,n+1):
        for x in range(1,m+1):
            for a,b in H:
                p=x+a
                q=y+b
                if 1<=p<=m and 1<=q<=n:
                    G.add_edge((x,y),(p,q))
    return G

#Pathグラフ
def Path_Graph(n):
    P=Graph()
    for i in range(1,n):
        P.add_edge(i,i+1)
    return P

#Cycleグラフ
def Cycle_Graph(n):
    C=Graph()
    for i in range(1,n):
        C.add_edge(i,i+1)
    C.add_edge(n,1)
    return C

#Starグラフ
def Star_Graph(n):
    S=Graph()
    for i in range(1,n+1):
        S.add_edge(0,i)
    return S

#Wheelグラフ
def Wheel_Graph(n):
    W=Graph()
    for i in range(1,n+1):
        W.add_edge(0,i)

    for j in range(n):
        W.add_edge(j%n+1,(j+1)%n+1)
    return W

#騎士巡回グラフ
def Knight_Tour_Graph(m,n,index=1,s=1,t=2):
    """
    """
    E=[]
    for x in range(index,m+index):
        E+=[(x,y) for y in range(index,n+index)]

    G=Graph(E)
    H=[(s,t),(t,s),(s,-t),(t,-s)]

    for y in range(index,n+index):
        for x in range(index,m+index):
            for a,b in H:
                p=x+a
                q=y+b
                if index<=p<m+index and index<=q<n+index:
                    G.add_edge((x,y),(p,q))
    return G

#完全k分木
def Complete_Kary_Tree(n,k=2):
    m=(k**n-1)//(k-1)
    T=Graph(range(m))

    for i in range(1,m):
        T.add_edge((i-1)//k,i)
    return T
#---------------------------------------
def One_Point_Distance(G,From,with_path=False):
    """単一始点Fromからの距離を求める.

    G:グラフ
    From:始点
    with_path:最短路も含めて出力するか?

    (出力の結果)
    with_path=True->(距離,最短経路の辿る際の前の頂点)
    with_path=False->距離
    """
    from copy import copy
    from collections import deque

    inf=float("inf")
    T={v:inf for v in G.adjacent}
    T[From]=0

    if with_path:
        Prev={v:None for v in G.adjacent}

    Q=deque([From])

    while Q:
        u=Q.popleft()

        for v in G.adjacent[u]:
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

    D:負Cycleを含まない有向グラフ
    """
    T={v:{} for v in D.vertex} #T[u][v]:uからvへ
    for u in D.vertex:
        for v in D.vertex:
            if v==u:
                T[u][v]=0
            elif v in D.adjacent_out[u]:
                T[u][v]=D.adjacent_out[u][v]
            else:
                T[u][v]=float("inf")

    for u in D.vertex:
        for v in D.vertex:
            for w in D.vertex:
                T[v][w]=min(T[v][w],T[v][u]+T[u][w])

    return T
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
    if prefunc:
        prefunc(v)

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

    if prefunc:
        prefunc(v)

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
=======
class Graph:
    #入力定義
    def __init__(self,vertex=[]):
        self.vertex=set(vertex)

        self.edge_number=0
        self.adjacent={v:set() for v in vertex}

    #頂点の追加
    def add_vertex(self,*adder):
        for v in adder:
            if not self.vertex_exist(v):
                self.adjacent[v]=set()
                self.vertex.add(v)

    #辺の追加
    def add_edge(self,u,v):
        self.add_vertex(u)
        self.add_vertex(v)

        if not self.edge_exist(u,v):
            self.adjacent[u].add(v)
            self.adjacent[v].add(u)
            self.edge_number+=1

    #辺を除く
    def remove_edge(self,u,v):
        self.add_vertex(u)
        self.add_vertex(v)

        if self.edge_exist(u,v):
            self.adjacent[u].discard(v)
            self.adjacent[v].discard(u)
            self.edge_number-=1

    #頂点を除く
    def remove_vertex(self,*vertexes):
        for v in vertexes:
            if self.vertex_exist(v):
                U=self.neighbohood(v)
                for u in U:
                    self.edge_number-=1
                    self.adjacent[u].discard(v)

                del self.adjacent[v]
                self.vertex.discard(v)

    #Walkの追加
    def add_walk(self,*walk):
        n=len(walk)
        for i in range(n-1):
            self.add_edge(walk[i],walk[i+1])

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
    def edge_exist(self,u,v):
        if not(self.vertex_exist(u) and self.vertex_exist(v)):
            return False
        return v in self.adjacent[u]

    #近傍
    def neighbohood(self,v):
        if not self.vertex_exist(v):
            return []
        return list(self.adjacent[v])

    #次数
    def degree(self,v):
        if not self.vertex_exist(v):
            return 0

        return len(self.adjacent[v])

    #頂点数
    def vertex_count(self):
        return len(self.vertex)

    #辺数
    def edge_count(self):
        return self.edge_number

    #頂点vを含む連結成分
    def connected_component(self,v):
        if v not in self.adjacent:
            return []

        from collections import deque
        T={u:0 for u in self.vertex}
        T[v]=1
        Q=deque([v])
        while Q:
            u=Q.popleft()
            for w in self.adjacent[u]:
                if not T[w]:
                    T[w]=1
                    Q.append(w)
        return [x for x in self.adjacent if T[x]]

    #距離
    def distance(self,u,v):
        from collections import deque
        inf=float("inf")
        T={v:inf  for v in self.vertex}

        if u==v:
            return 0
        Q=deque([u])
        T[u]=0
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
        from collections import deque
        inf=float("inf")
        T={v:inf  for v in self.vertex}

        Q=deque([u])
        T[u]=0
        while Q:
            w=Q.popleft()
            for x in self.adjacent[w]:
                if T[x]==inf:
                    T[x]=T[w]+1
                    Q.append(x)
        return T

    #最短路
    def shortest_path(self,u,v):
        from collections import deque
        inf=float("inf")
        T={v:None for v in self.vertex}

        if u==v:
            return [u]

        Q=deque([u])
        T[u]=u
        while Q:
            w=Q.popleft()
            for x in self.adjacent[w]:
                if not T[x]:
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

    #何かしらの頂点を選ぶ.
    def poping_vertex(self):
        v=self.vertex.pop()
        self.vertex.add(v)
        return v


G=Graph()
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(4,1)
G.add_edge(5,6)
G.add_edge(6,7)
G.add_edge(5,7)
G.add_edge(1,7)

#FromからToへの(長さが丁度L or L以下の)Walkが存在するか否か
def walk_exist(graph,From,To,L,just=False):
    if L<0:
        return False
    if From==To and just==False:
        return True
    if From==To and just==True and L==0:
        return True

    F=False
    for w in graph.neighbohood(From):
        if graph.edge_exist(From,w):
            F=F or walk_exist(graph,w,To,L-1,just=just)
    return F

#補グラフの作成
def Complement_Graph(G):
    import copy
    n=len(G.vertex)
    H=Graph(copy.deepcopy(G.vertex))
    for j in range(n):
        for i in range(j+1,n):
            if G.adjacent[j][i]==0:
                H.add_edge(G.vertex[i],G.vertex[j])
    return H

#n頂点のランダムグラフ
def Random_Graph(n,p=0.5,seed=None):
    import random
    G=Empty_Graph(n)
    if p<0:p=0
    elif p>1:p=1

    random.seed(seed)
    for j in range(1,n+1):
        for i in range(j+1,n+1):
            if random.random()<p:
                G.add_edge(i,j)
    return G

#連結グラフ?
def Is_Connected(G):
    from collections import deque
    T={u:False for u in G.vertex}
    v=G.poping_vertex()

    Q=deque([v])
    Q_popleft=Q.popleft
    Q_append=Q.append
    K=0
    while Q:
        u=Q_popleft()
        for w in G.adjacent[u]:
            if not T[w]:
                T[w]=True
                Q_append(w)
                K+=1

    return (K==G.vertex_count())

#木?
def Is_Tree(G):
    if G.edge_count()!=len(G.vertex)-1:
        return False
    return Is_Connected(G)

#木の直径
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
    T={v:False for v in G.vertex}
    C=[]
    for v in G.vertex:
        if not T[v]:
            X=G.connected_component(v)
            for x in X:
                T[x]=True
            C.append(X)
    return C

#連結成分の個数
def Connected_Component_Number(G):
    T={v:False for v in G.vertex}
    C=0
    for v in G.vertex:
        if not T[v]:
            X=G.connected_component(v)
            for x in X:
                T[x]=True
            C+=1
    return C

#Cycleが存在する?
def Is_Exist_Cycle(G):
    from collections import deque
    T={u:False for u in G.vertex}

    for v in G.vertex:
        if not T[v]:
            x=v
            T[v]=True
            S=deque([v])
            while S:
                u=S.popleft()
                for w in G.neighbohood(u):
                    if not T[w]:
                        T[w]=True
                        S.append(w)
                    elif x!=w:
                        return True
                x=u

    return False

#2部グラフ?
def Is_Bipartite_Graph(G):
    from collections import deque
    T={u:0 for u in G.vertex}

    for v in G.vertex:
        if not T[v]:
            x=v
            T[v]=1
            S=deque([v])
            while S:
                u=S.popleft()
                for w in G.adjacent[u]:
                    if T[w]==0:
                        T[w]=-T[u]
                        S.append(w)
                    elif T[w]==T[u]:
                        return False
                x=u

    return True

#2部グラフの部集合に分割
def Bipartite_Separate(G):
    from collections import deque
    T={u:0 for u in G.vertex}

    for v in G.vertex:
        if not T[v]:
            x=v
            T[v]=1
            S=deque([v])
            while S:
                u=S.popleft()
                for w in G.adjacent[u]:
                    if T[w]==0:
                        T[w]=-T[u]
                        S.append(w)
                    elif T[w]==T[u]:
                        return None
                x=u

    U=[u for u in G.vertex if T[u]==1]
    V=[v for v in G.vertex if T[v]==-1]
    return U,V

#オイラーグラフ?
def Is_Eulerian_Graph(G):
    for v in G.vertex:
        if G.degree(v)%2:
            return False
    return True

#純オイラーグラフ?
def Is_Semi_Eulerian_Graph(G):
    K=0
    for v in G.vertex:
        if G.degree(v)%2:
            K+=1
            if K==3:
                return False
    return K==2

#純オイラーグラフ?
def Find_Eulerian_Trail(G):
    U=[]
    K=0
    for v in G.vertex:
        if G.degree(v)%2:
            K+=1
            U.append(v)

            if K==3:
                return False

#Euler閉路を見つける
def Find_Eulerian_Cycle(G):
    from copy import deepcopy

    if not Is_Eulerian_Graph(G):
        return None

    N=len(G.vertex)
    K=G.vertex_count()
    A=deepcopy(G.adjacent)

    U,V=G.vertex[0],G.vertex[-1]
    X=U
    P=[U]

    while X!=V:
        X=G.neighbohood(X)[0]
        P.append(X)

    print(P)

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
def Complete_Graph(n):
    G=Graph([i+1 for i in range(n)])
    for v in range(1,n+1):
        for u in range(v+1,n+1):
            G.add_edge(u,v)
    return G

#完全2部グラフ
def Complete_Bipartite_Graph(m,n):
    X=list(range(-1,-(m+1),-1))+list(range(1,n+1))
    G=Graph(X)

    for x in range(1,m+1):
        for y in range(1,n+1):
            G.add_edge(-x,y)

    return G

#グラフ作成
def Making_Graph(V,E):
    S=set(V)
    for e in E:
        try:
            if len(e)!=2:
                return None
        except:
            return None
        a,b=e

    G=Graph(V)

    for e in E:
        G.add_edge(*e)
    return G

#空グラフの作成
def Empty_Graph(n):
    return Graph(list(range(1,n+1)))

#ペテルセングラフ
def Petersen_Graph(n=5,k=2):
    V=list(range(1,n+1))+list(range(-1,-(n+1),-1))

    G=Graph(V)
    for i in range(n):
        G.add_edge(i+1,-(i+1))
        G.add_edge(i+1,(i+1)%n+1)
        G.add_edge(-(i+1),-((i+k)%n+1))
    return G

#格子グラフ
def Grid_Graph(m,n):
    """m x n マスのグラフを生成する.
    """
    E=[]
    for x in range(1,m+1):
        E+=[(x,y) for y in range(1,n+1)]

    G=Graph(E)
    H=[(1,0),(0,1)]

    for y in range(1,n+1):
        for x in range(1,m+1):
            for a,b in H:
                p=x+a
                q=y+b
                if 1<=p<=m and 1<=q<=n:
                    G.add_edge((x,y),(p,q))
    return G

#Pathグラフ
def Path_Graph(n):
    P=Graph()
    for i in range(1,n):
        P.add_edge(i,i+1)
    return P

#Cycleグラフ
def Cycle_Graph(n):
    C=Graph()
    for i in range(1,n):
        C.add_edge(i,i+1)
    C.add_edge(n,1)
    return C

#Starグラフ
def Star_Graph(n):
    S=Graph()
    for i in range(1,n+1):
        S.add_edge(0,i)
    return S

#Wheelグラフ
def Wheel_Graph(n):
    W=Graph()
    for i in range(1,n+1):
        W.add_edge(0,i)

    for j in range(n):
        W.add_edge(j%n+1,(j+1)%n+1)
    return W

#騎士巡回グラフ
def Knight_Tour_Graph(m,n,index=1,s=1,t=2):
    """
    """
    E=[]
    for x in range(index,m+index):
        E+=[(x,y) for y in range(index,n+index)]

    G=Graph(E)
    H=[(s,t),(t,s),(s,-t),(t,-s)]

    for y in range(index,n+index):
        for x in range(index,m+index):
            for a,b in H:
                p=x+a
                q=y+b
                if index<=p<m+index and index<=q<n+index:
                    G.add_edge((x,y),(p,q))
    return G

#完全k分木
def Complete_Kary_Tree(n,k=2):
    m=(k**n-1)//(k-1)
    T=Graph(range(m))

    for i in range(1,m):
        T.add_edge((i-1)//k,i)
    return T
#---------------------------------------
def One_Point_Distance(G,From,with_path=False):
    """単一始点Fromからの距離を求める.

    G:グラフ
    From:始点
    with_path:最短路も含めて出力するか?

    (出力の結果)
    with_path=True->(距離,最短経路の辿る際の前の頂点)
    with_path=False->距離
    """
    from copy import copy
    from collections import deque

    inf=float("inf")
    T={v:inf for v in G.adjacent}
    T[From]=0

    if with_path:
        Prev={v:None for v in G.adjacent}

    Q=deque([From])

    while Q:
        u=Q.popleft()

        for v in G.adjacent[u]:
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

    D:負Cycleを含まない有向グラフ
    """
    T={v:{} for v in D.vertex} #T[u][v]:uからvへ
    for u in D.vertex:
        for v in D.vertex:
            if v==u:
                T[u][v]=0
            elif v in D.adjacent_out[u]:
                T[u][v]=D.adjacent_out[u][v]
            else:
                T[u][v]=float("inf")

    for u in D.vertex:
        for v in D.vertex:
            for w in D.vertex:
                T[v][w]=min(T[v][w],T[v][u]+T[u][w])

    return T
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
    if prefunc:
        prefunc(v)

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

    if prefunc:
        prefunc(v)

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
>>>>>>> c43297b8f7390d871b65dde0d6454412f7e7a8ca
