class Tree:
    __slots__=("N", "index", "parent", "__mutable",
            "root", "children", "depth", "tower", "upper_list", "deg", "des_count", "preorder_number",
            "euler", "in_time", "out_time")

    def __init__(self,N,index=0):
        """ N 頂点 (index, index+1, ..., N-1+index) の根付き木を生成する. """
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

        self.root=root

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
        assert hasattr(self,"root")

        a=self.index
        b=self.index+self.N
        C=[[] for _ in range(b)]

        p=self.parent
        ve=self.vertex_exist
        for i in range(a,b):
            if i!=self.root:
                assert ve(p[i])
                C[p[i]].append(i)

        self.__mutable=False
        self.children=C

    #データを求める.
    def depth_search(self,Mode=True):
        """ 木の深さを求める. """

        assert self.__after_seal_check()

        if hasattr(self,"depth"):
            if Mode:
                return self.depth
            else:
                return

        from collections import deque
        C=self.children
        D=[-1]*(self.index+self.N)
        E=[[] for _ in range(self.N)]

        Q=deque([self.root])
        D[self.root]=0
        E[0]=[self.root]

        while Q:
            x=Q.popleft()
            d=D[x]
            for y in C[x]:
                D[y]=d+1
                E[d+1].append(y)
                Q.append(y)

        self.depth=D
        self.tower=E

        if Mode:
            return D

    def vertex_depth(self,x):
        """ 頂点 x の深さを求める."""

        assert self.__after_seal_check(x)

        if not hasattr(self,"depth"):
            self.depth_search(Mode=False)
        return self.depth[x]

    def __upper_list(self):
        assert self.__after_seal_check()

        if hasattr(self,"upper_list"):
            return

        if not hasattr(self,"depth"):
            self.depth_search(False)

        b=max(self.depth).bit_length()
        X=[[-1]*(self.index+self.N) for _ in range(b)]

        Y=X[0]
        p=self.parent
        rg=range(self.index,self.index+self.N)

        for x in rg:
            if x!=self.root:
                Y[x]=p[x]
            else:
                Y[x]=self.root

        for k in range(1,b):
            Y=X[k-1]
            Z=X[k]

            for x in rg:
                Z[x]=Y[Y[x]]
        self.upper_list=X

    def upper(self,x,k,over=True):
        """ 頂点 x から見て k 個親の頂点を求める.

        over: (頂点 x の深さ)<k のときに True ならば根を返し, False ならばエラーを吐く.
        """

        assert self.__after_seal_check(x)
        assert 0<=k

        if not hasattr(self,"upper_list"):
            self.__upper_list()

        if self.vertex_depth(x)<k:
            if over:
                return self.root
            else:
                raise ValueError

        i=0
        while k:
            if k&1:
                x=self.upper_list[i][x]
            k>>=1
            i+=1
        return x

    def lowest_common_ancestor(self,x,y):
        """ 頂点 x, y の最小共通先祖 (x,yに共通する先祖で最も深いもの) を求める. """

        assert self.__after_seal_check(x,y)

        dd=self.vertex_depth(y)-self.vertex_depth(x)
        if dd<0:
            x,y=y,x
            dd=-dd

        y=self.upper(y,dd)
        if x==self.root:
            return x
        if x==y:
            return x

        d=self.vertex_depth(x)
        b=d.bit_length()

        X=self.upper_list
        for k in range(b-1,-1,-1):
            px=X[k][x];py=X[k][y]
            if px!=py:
                x=px;y=py

        return self.upper(x,1)

    def __degree_count(self):
        assert self.__after_seal_check()

        if hasattr(self,"deg"):
            return

        self.deg=[0]*(self.index+self.N)
        for v in range(self.index,self.index+self.N):
            d=len(self.children[v])+1
            if d==self.root:
                d-=1
            self.deg[v]=d
        return

    def degree(self,v):
        """ 頂点 v の次数を求める. """

        assert self.__after_seal_check(v)

        if not hasattr(self,"deg"):
            self.__degree_count()
        return self.deg[v]

    def diameter(self):
        """ 木の直径を求める."""

        assert self.__after_seal_check()

        from collections import deque
        def bfs(start):
            X=[-1]*(self.index+self.N)
            Q=deque([start])
            X[start]=0

            pa=self.parent
            ch=self.children
            while Q:
                x=Q.popleft()

                if X[pa[x]]==-1:
                    Q.append(pa[x])
                    X[pa[x]]=X[x]+1

                for y in ch[x]:
                    if X[y]==-1:
                        Q.append(y)
                        X[y]=X[x]+1
            y=max(range(self.index,self.index+self.N),key=lambda x:X[x])
            return y,X[y]

        y,_=bfs(self.root)
        z,d=bfs(y)
        return d,(y,z)

    def path(self,u,v):
        """ 頂点 u, v 間のパスを求める. """

        assert self.__after_seal_check(u,v)

        w=self.lowest_common_ancestor(u,v)
        pa=self.parent

        X=[u]
        while u!=w:
            u=pa[u]
            X.append(u)

        Y=[v]
        while v!=w:
            v=pa[v]
            Y.append(v)
        return X+Y[-2::-1]

    def is_brother(self,u,v):
        """ 2つの頂点 u, v は兄弟 (親が同じ) か?  """

        assert self.__after_seal_check(u,v)

        if u==self.root or v==self.root:
            return False
        return self.parent[u]==self.parent[v]

    def is_ancestor(self,u,v):
        """ 頂点 u は頂点 v の先祖か? """

        assert self.__after_seal_check(u,v)

        dd=self.vertex_depth(v)-self.vertex_depth(u)
        if dd<0:
            return False

        v=self.upper(v,dd)
        return u==v

    def is_descendant(self,u,v):
        """ 頂点 u は頂点 v の子孫か? """

        assert self.__after_seal_check(u,v)
        return self.is_ancestor(v,u)

    def is_leaf(self,v):
        """ 頂点 v は葉? """

        return not bool(self.children[v])

    def distance(self,u,v):
        """ 2頂点 u, v 間の距離を求める. """

        assert self.__after_seal_check(u,v)

        dep=self.vertex_depth
        return dep(u)+dep(v)-2*dep(self.lowest_common_ancestor(u,v))

    def __descendant_count(self):
        assert self.__after_seal_check()
        if hasattr(self,"des_count"):
            return

        if not hasattr(self,"tower"):
            self.depth_search(False)

        self.des_count=[1]*(self.index+self.N)
        pa=self.parent
        for T in self.tower[:0:-1]:
            for x in T:
                self.des_count[pa[x]]+=self.des_count[x]
        return

    def descendant_count(self, v):
        """ 頂点 v の子孫の数を求める. """
        assert self.__after_seal_check(v)
        self.__descendant_count()
        return self.des_count[v]

    def subtree_size(self, v):
        """ 頂点 v を根とした部分根付き木のサイズを求める. """
        return self.descendant_count(v)

    def preorder(self,v):
        """ 頂点 v の行きがけ順を求める. """
        assert self.__after_seal_check(v)
        if hasattr(self,"preorder_number"):
            self.preorder_number[v]

        from collections import deque
        Q=deque([self.root])
        T=[-1]*(self.N+self.index)

        p=1
        while Q:
            x=Q.popleft()
            T[x]=p
            p+=1

            C=self.children[x]
            for y in C:
                Q.append(y)
        self.preorder_number=T
        return T[v]

    def dfs_yielder(self):
        """ DFS における頂点の出入りを yield する.

        (v,1): 頂点 v に入る
        (v,0): 頂点 v を出る
        """
        assert self.__after_seal_check()

        #最初
        yield (self.root,1)

        v=self.root

        ch=self.children
        pa=self.parent

        R=[-1]*self.index+[len(ch[x]) for x in range(self.index,self.index+self.N)]
        S=[0]*(self.index+self.N)

        while True:
            if R[v]==S[v]:  #もし,進めないならば
                yield (v,0) #頂点vを出る
                if v==self.root:
                    break
                else:
                    v=pa[v]
            else:   #進める
                w=v
                v=ch[v][S[v]]
                S[w]+=1
                yield (v,1)

    def top_down(self):
        """ 木の頂点から yield する. """

        assert self.__after_seal_check()
        if not hasattr(self,"tower"):
            self.depth_search(False)

        for E in self.tower:
            for v in E:
                yield v

    def bottom_up(self):
        """ 木の根から yield する. """

        assert self.__after_seal_check()
        if not hasattr(self,"tower"):
            self.depth_search(False)

        for E in self.tower[::-1]:
            for v in E:
                yield v

    def tree_dp_from_leaf(self,merge,unit,f,g,Mode=False):
        """ 葉から木 DP 行う.

        [input]
        merge: 可換モノイドを成す2項演算 M x M -> M
        unit: Mの単位元
        f: X x V x V → M: f(x,v,w): v が親, w が子
        g: M x V → X: g(x,v)
        Mode: False → 根の値のみ, True → 全ての値

        [補足]
        頂点 v の子が x,y,z,...のとき, 更新式は * を merge として
            dp[v]=g(f(dp[x],v,x)*f(dp[y],v,y)*f(dp[z],v,z)*..., v)
        になる.
        """
        assert self.__after_seal_check()

        data=[unit]*(self.index+self.N)
        ch=self.children

        for x in self.bottom_up():
            for y in ch[x]:
                data[x]=merge(data[x],f(data[y],x,y))
            data[x]=g(data[x],x)

        if Mode:
            return data
        else:
            return data[self.root]

    def tree_dp_from_root(self,f,alpha):
        """ 根から木 DP を行う.

        [input]
        alpha: 初期値
        f: X x V x V -> X: f(x,v,w): v が親, w が子

        [補足]
        頂点 v の親が x のとき, 更新式は
            dp[v]=f(dp[x],x,v) (x!=root), alpha (x==root)
        になる.
        """
        assert self.__after_seal_check()

        data=[0]*(self.index+self.N)
        ch=self.children

        data[self.root]=alpha
        for x in self.top_down():
            for y in ch[x]:
                data[y]=f(data[x],x,y)

        return data

    def rerooting(self,merge,unit,f,g):
        """ 全方位木 DP を行う.

        [input]
        calc:可換モノイドを成す2項演算 M x M -> M
        unit:Mの単位元
        f: X x V x V -> M: f(x,v,w): v が親, w が子
        g: M x V -> X: g(x,v)

        ※ tree_dp_from_leaf と同じ形式

        [補足]
        頂点 v の子が x,y,z,...のとき, 更新式は
        dp[v]=g(f(dp[x],v,x)*f(dp[y],v,y)*f(dp[z],v,z)*..., v)
        になる.
        """
        assert self.__after_seal_check()

        upper=[unit]*(self.index+self.N)
        lower=[unit]*(self.index+self.N)

        ch=self.children
        pa=self.parent

        #DFSパート
        lower=self.tree_dp_from_leaf(merge,unit,f,g,True)

        #BFSパート
        for v in self.top_down():
            cc=ch[v]

            #累積マージ
            deg=len(cc)

            Left=[unit]; x=unit
            for c in cc:
                x=merge(x,f(lower[c],v,c))
                Left.append(x)

            Right=[unit]; y=unit
            for c in cc[::-1]:
                y=merge(y,f(lower[c],v,c))
                Right.append(y)
            Right=Right[::-1]

            for i in range(deg):
                c=cc[i]

                a=merge(Left[i],Right[i+1])

                if v!=self.root:
                    b=merge(a,f(upper[v],v,pa[v]))
                else:
                    b=a

                upper[c]=g(b,v)

        A=[unit]*(self.index+self.N)
        for v in range(self.index,self.index+self.N):
            if v!=self.root:
                a=f(upper[v],v,pa[v])
            else:
                a=unit

            for c in ch[v]:
                a=merge(a,f(lower[c],v,c))
            A[v]=g(a,v)
        return A

    def euler_tour(self):
        """ オイラーツアーに関する計算を行う. """

        assert self.__after_seal_check()
        if hasattr(self,"euler"):
            return

        #最初
        X=[]; X_append=X.append #X: Euler Tour のリスト

        v=self.root

        ch=self.children
        pa=self.parent

        R=[-1]*self.index+[len(ch[x]) for x in range(self.index,self.index+self.N)]
        S=[0]*(self.index+self.N)
        while True:
            X_append(v)
            if R[v]==S[v]:  #もし,進めないならば
                if v==self.root:
                    break
                else:
                    v=pa[v]
            else:   #進める
                w=v
                v=ch[v][S[v]]
                S[w]+=1

        self.euler=X
        self.in_time=[-1]*(self.index+self.N)
        self.out_time=[-1]*(self.index+self.N)
        for i in range(len(X)):
            v=X[i]
            if self.in_time[v]==-1:
                self.in_time[v]=self.out_time[v]=i
            else:
                self.out_time[v]=i

    def centroid(self, all=False):
        """ 木の重心を求める

        all: False → 重心のうちの1頂点. True → 全ての重心.
        """

        assert self.__after_seal_check()

        M=self.N//2

        if not hasattr(self,"des_count"):
            self.__descendant_count()

        G=[]; ch=self.children; des=self.des_count

        for v in range(self.index, self.index+self.N):
            if self.N-des[v]>M:
                break

            flag=1
            for x in ch[v]:
                if des[x]>M:
                    flag=0
                    break
            if flag:
                if all:
                    G.append(v)
                else:
                    return v
        return G

#=================================================
def Making_Tree(N,E,root,index=0):
    """木を作る.

    N:頂点数
    E: 辺のリスト
    root: 根
    """

    from collections import deque
    F=[[] for _ in range(index+N)]
    for u,v in E:
        assert index<=u<index+N
        assert index<=v<index+N
        assert u!=v

        F[u].append(v)
        F[v].append(u)

    X=[-1]*(index+N)
    X[root]=root

    C=[[] for _ in range(index+N)]

    Q=deque([root])
    while Q:
        x=Q.popleft()
        for y in F[x]:
            if X[y]==-1:
                X[y]=x
                Q.append(y)
                C[x].append(y)

    T=Tree(N,index)
    T.root_set(root)
    T.parent=X
    T.children=C
    T.seal()
    return T

def Spanning_Tree(N,E,root,index=0,exclude=False):
    """ 連結なグラフから全域木をつくる.

    N: 頂点数
    E:  辺のリスト
    root: 根
    exclude: 全域木から外れた辺のリストを出力するか.
    """

    from collections import deque
    F=[set() for _ in range(index+N)]
    EE=[]
    L=[]
    for u,v in E:
        assert index<=u<index+N
        assert index<=v<index+N

        if (u==v) or (u in F[v]):
            L.append((u,v))
            continue

        EE.append((u,v))
        F[u].add(v)
        F[v].add(u)

    X=[-1]*(index+N)
    X[root]=root

    C=[[] for _ in range(index+N)]

    Q=deque([root])
    while Q:
        x=Q.popleft()
        for y in F[x]:
            if X[y]==-1:
                X[y]=x
                Q.append(y)
                C[x].append(y)

    T=Tree(N,index)
    T.root_set(root)
    T.parent=X
    T.children=C
    T.seal()

    if exclude==False:
        return T

    pa=T.parent
    for u,v in EE:
        if not(pa[v]==u or pa[u]==v):
            L.append((u,v))

    return T,L
