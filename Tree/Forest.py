from Tree import *

class Forest():
    def __init__(self, N, index=0):
        self.N=N
        self.index=index
        self.parent=[-1]*(N+index)
        self.__mutable=True

    def vertex_exist(self,x):
        """ 頂点 x が存在するかどうかを判定する. """

        return self.index<=x<self.index+self.N

    def __after_seal_check(self,*vertexes):
        """ 木が確定していて, vertexes の頂点が存在するかどうかをチェックする. """

        if self.__mutable:
            return False

        for v in vertexes:
            if not self.vertex_exist(v):
                return False
        return True

    def is_mutable(self):
        """ 木が確定して [いない] かどうかを返す. """
        return self.__mutable

    #設定パート
    def root_set(self,root):
        """ 頂点 x を根に設定する."""

        assert self.vertex_exist(root)
        assert self.__mutable

        self.parent[root]=-1

    def parent_set(self,x,y):
        """ 頂点 x の親を y に設定する."""

        assert self.vertex_exist(x)
        assert self.vertex_exist(y)
        assert self.__mutable

        self.parent[x]=y

    def child_set(self,x,y):
        """ 頂点 x の子の一つに y を設定する."""

        assert self.vertex_exist(x)
        assert self.vertex_exist(y)
        assert self.__mutable

        self.parent[y]=x

    def seal(self):
        """ 木の情報を確定させる."""

        assert self.__mutable
        from collections import deque

        a=self.index
        b=self.index+self.N
        C=[[] for _ in range(b)]

        self.component_id=[-1]*b
        self.vertex_number=[0]*b
        self.vertex=[]
        self.root=[]
        
        pa=self.parent
        ve=self.vertex_exist

        for w in range(a,b):
            if pa[w]!=-1:
                C[pa[w]].append(w)

        m=0
        k=0
        for v in range(a,b):
            if pa[v]!=-1:
                continue

            self.root.append(v)
            i=0

            self.component_id[v]=k
            self.vertex.append([])

            Q=deque([v])
            while Q:
                w=Q.popleft()
                m+=1
                self.vertex_number[w]=i; i+=1
                self.vertex[-1].append(w)

                for u in C[w]:
                    if self.component_id[u]==-1:
                        self.component_id[u]=k
                        Q.append(u)
            k+=1

        assert m==self.N           

        self.__mutable=False
        self.tree=[]
        for j in range(k):
            T=Tree(len(self.vertex[j]))

            T.root_set(0)
            for v in self.vertex[j]:
                for w in C[v]:
                    T.parent_set(self.vertex_number[w], self.vertex_number[v])

            T.seal()
            self.tree.append(T)

        self.children=C
        self.component_number=k

    def depth_search(self, Mode=True):
        """ 各頂点の深さを求める. """

        assert self.__after_seal_check()
        if hasattr(self,"depth"):
            if Mode:
                return self.depth
            else:
                return

        for T in self.tree:
            M=T.depth_search(1)

        self.depth=[0]*(self.N+self.index)
        ve=self.vertex
        nu=self.vertex_number
        for k in range(self.component_number):
            T=self.tree[k]
            for i,v in enumerate(ve[k]):
                self.depth[v]=T.vertex_depth(i)

        if Mode:
            return self.depth

    def vertex_depth(self,x):
        """ 頂点 x の深さを求める."""

        assert self.__after_seal_check(x)

        if not hasattr(self,"depth"):
            self.depth_search(Mode=False)
        return self.depth[x]

    def dfs_yielder(self):
        """ DFS における頂点の出入りを yield する.

        (v,1): 頂点 v に入る
        (v,0): 頂点 v を出る
        (-1,-1): その木での yield が終了
        """

        for k,T in enumerate(self.tree):
            v=self.vertex[k]
            for i,c in T.dfs_yielder():
                yield v[i],c
            yield -1,-1

    def top_down(self):
        """ 木の頂点から yield する.
        ※ -1 でその木での yield が終了
        """

        assert self.__after_seal_check()
        if not hasattr(self,"depth"):
            self.depth_search(False)

        for k,T in enumerate(self.tree):
            v=self.vertex[k]
            for i in T.top_down():
                yield v[i]
            yield -1

    def bottom_up(self):
        """ 木の根から yield する. """

        assert self.__after_seal_check()
        if not hasattr(self,"depth"):
            self.depth_search(False)

        for k,T in enumerate(self.tree):
            v=self.vertex[k]
            for i in T.bottom_up():
                yield v[i]
            yield -1

    def is_connect(self, x, y):
        """ 頂点 x, y が同じ連結成分かどうかを判定する."""

        assert self.__after_seal_check(x,y)
        return self.component_id[x]==self.component_id[y]

#=================================================
def Making_Forest(N, E, root_priority=None, index=0):
    """ 森を作る.

    N: 頂点数
    E: 辺のリスト
    root_priority: 各連結成分の根になりうる頂点の優先順位
    """

    if root_priority==None:
        root_priority=range(index, index+N)

    from collections import deque
    G=[[] for _ in range(index+N)]
    for u,v in E:
        assert index<=u<index+N
        assert index<=v<index+N
        assert u!=v

        G[u].append(v)
        G[v].append(u)

    X=[-1]*(index+N)
    S=[0]*(index+N)

    for root in root_priority:
        if X[root]!=-1:
            continue

        Q=deque([root]); S[root]=1
        while Q:
            x=Q.popleft()
            for y in G[x]:
                if S[y]==0:
                    X[y]=x
                    S[y]=1
                    Q.append(y)

    F=Forest(N,index)
    for x in range(index, index+N):
        if X[x]!=-1:
            F.parent_set(x,X[x])
    F.seal()
    return F

def Spanning_Forest(N, E, root_priority=None, index=0, exclude=0):
    """ 全域森をつくる.

    N: 頂点数
    E:  辺のリスト
    root_priority: 各連結成分の根になりうる頂点の優先順位
    exclude: 全域森から外れた辺のリストの出力方法
        0 → なし
        1 → 除外辺を出力
        2 → 除外辺を連結成分毎にわける
    """

    from collections import deque,defaultdict
    G=[set() for _ in range(index+N)]
    M=[]
    EE=[]
    for u,v in E:
        assert index<=u<index+N
        assert index<=v<index+N

        if (u==v) or (u in G[v]):
            M.append((u,v))
            continue

        G[u].add(v)
        G[v].add(u)
        EE.append((u,v))

    X=[-1]*(index+N)
    S=[0]*(index+N)

    if root_priority==None:
        root_priority=range(index, index+N)

    for root in root_priority:
        if X[root]!=-1:
            continue

        Q=deque([root]); S[root]=1
        while Q:
            x=Q.popleft()
            for y in G[x]:
                if S[y]==0:
                    X[y]=x
                    S[y]=1
                    Q.append(y)

    F=Forest(N,index)
    for x in range(index, index+N):
        if X[x]!=-1:
            F.parent_set(x,X[x])
    F.seal()

    if exclude==0:
        return F
    elif exclude==1:
        for u,v in EE:
            if not (X[v]==u or X[u]==v):
                M.append((u,v))
        return F,M
    else:
        comp=F.component_id
        L=[[] for _ in range(F.component_number)]

        for u,v in M:
            k=comp[u]
            L[k].append((u,v))

        for u,v in EE:
            if not (X[v]==u or X[u]==v):
                k=comp[u]
                L[k].append((u,v))
        return F,L
