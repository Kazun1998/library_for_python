class Tree:
    __slots__=("N", "index", "parent", "__mutable",
            "root", "children", "depth", "tower", "upper_list", "des_count", "preorder_number",
            "euler_vertex", "euler_edge", "in_time", "out_time", "lca_dst",
            "hld_hedge")

    def __init__(self, N, index=0):
        """ N 頂点 (index, index+1, ..., N-1+index) の根付き木を生成する. """
        self.N=N
        self.index=index
        self.parent=[-1]*(N+index)
        self.__mutable=True

    def vertex_exist(self, x):
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
    def root_set(self, root):
        """ 頂点 root を根に設定する."""

        assert self.vertex_exist(root)
        assert self.__mutable

        self.root=root

    def parent_set(self,x,y):
        """ 頂点 x の親を y に設定する."""

        assert self.vertex_exist(x)
        assert self.vertex_exist(y)
        assert self.__mutable

        self.parent[x]=y

    def child_set(self, x, y):
        """ 頂点 x の子の一つに y を設定する (頂点 x の方が親)."""

        assert self.vertex_exist(x)
        assert self.vertex_exist(y)
        assert self.__mutable

        self.parent[y]=x

    def seal(self):
        """ 木の情報を確定させる (これ以降, 情報の変更は禁止)."""

        assert self.__mutable
        assert hasattr(self, "root")

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
    def depth_search(self, mode=True):
        """ 木の深さを求める.

        mode=True ならば, 各頂点の深さが記録されたリストを返す."""

        assert self.__after_seal_check()

        if hasattr(self, "depth"):
            if mode:
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

        if mode:
            return D

    def vertex_depth(self, x):
        """ 頂点 x の深さを求める."""

        assert self.__after_seal_check(x)

        if not hasattr(self, "depth"):
            self.depth_search(mode=False)
        return self.depth[x]

    def __upper_list(self):
        assert self.__after_seal_check()

        if hasattr(self, "upper_list"):
            return

        if not hasattr(self,"depth"):
            self.depth_search(False)

        b=max(self.depth).bit_length()
        X=[[-1]*(self.index+self.N) for _ in range(b)]

        Y=X[0]
        p=self.parent

        for x in range(self.index,self.index+self.N):
            if x!=self.root:
                Y[x]=p[x]
            else:
                Y[x]=self.root

        for k in range(1,b):
            Y=X[k-1]
            Z=X[k]

            for x in range(self.index,self.index+self.N):
                Z[x]=Y[Y[x]]
        self.upper_list=X

    def upper(self, x, k, over=True):
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

    def lowest_common_ancestor_greedy(self, x, y):
        """頂点 x, y の最小共通先祖 (x,yに共通する先祖で最も深いもの) を "愚直に" 求める."""

        assert self.__after_seal_check(x,y)
        dx=self.vertex_depth(x); dy=self.vertex_depth(y)

        if dx<dy:
            dx,dy=dy,dx
            x,y=y,x

        pa=self.parent
        while dx>dy:
            x=pa[x]
            dx-=1

        while x!=y:
            x=pa[x]
            y=pa[y]

        return x

    def __lca_prepare(self):
        assert self.__after_seal_check()

        N=self.N

        bit=max(1, ((2*N-1)-1).bit_length())
        D=[[0]*(2*N-1) for _ in range(bit)]

        self.euler_tour_vertex()
        tour=self.euler_vertex
        D[0]=tour.copy()
        dep=self.depth_search(True)

        for i in range(1, bit):
            shift=1<<i
            tab=D[i]

            for j in range(0, 2*N-1, 2*shift):
                t=min(j+shift, 2*N-1)
                tab[t-1]=tour[t-1]

                for k in range(t-2, j-1, -1):
                    if dep[tour[k]]<dep[tab[k+1]]:
                        tab[k]=tour[k]
                    else:
                        tab[k]=tab[k+1]

                if 2*N-1<=t:
                    break

                tab[t]=tour[t]
                r=min(t+shift, 2*N-1)

                for k in range(t+1, r):
                    if dep[tab[k-1]]<dep[tour[k]]:
                        tab[k]=tab[k-1]
                    else:
                        tab[k]=tour[k]

        self.lca_dst=D
        return

    def lowest_common_ancestor(self, x, y):
        """頂点 x, y の最小共通先祖 (x,yに共通する先祖で最も深いもの) を "高速に" 求める. """

        assert self.__after_seal_check(x,y)
        if not hasattr(self, "lca_dst"):
            self.__lca_prepare()

        a=self.in_time[x]; b=self.in_time[y]
        if a>b:
            x,y=y,x
            a,b=b,a

        if a==b:
            return self.lca_dst[0][a]

        p=(a^b).bit_length()-1
        tab=self.lca_dst[p]
        u=tab[a]; v=tab[b]

        return u if self.vertex_depth(u)<self.vertex_depth(v) else v

    def degree(self,v):
        """ 頂点 v の次数を求める. """

        assert self.__after_seal_check(v)
        if v==self.root:
            return len(self.children[v])
        else:
            return len(self.children[v])+1

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
            y=max(range(self.index,self.index+self.N), key=lambda x:X[x])
            return y,X[y]

        y,_=bfs(self.root)
        z,d=bfs(y)
        return d,(y,z)

    def path(self, u, v, faster=False):
        """ 頂点 u, v 間のパスを求める. """

        assert self.__after_seal_check(u,v)

        if faster:
            w=self.lowest_common_ancestor(u,v)
        else:
            w=self.lowest_common_ancestor_greedy(u,v)

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

    def is_parent(self, u, v):
        """ u は v の親か? """

        assert self.__after_seal_check(u,v)
        return v!=self.root and u==self.parent[v]

    def is_children(self, u, v):
        """ u は v の子か? """

        assert self.__after_seal_check(u,v)
        return self.is_parent(v,u)

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

    def direction(self, u, v):
        """ 頂点 u から頂点 v (u!=v) へ向かうパスが頂点 u の次に通る頂点"""

        assert self.__after_seal_check(u,v)
        assert u!=v

        if self.is_ancestor(u,v):
            du=self.vertex_depth(u)
            dv=self.vertex_depth(v)
            return self.upper(v,dv-(du+1))
        else:
            return self.parent[u]

    def jump(self, u, v, k, default=-1):
        """ 頂点 u から頂点 v へ向かうパスにおいて k 番目 (0-indexed) に通る頂点 (パスの長さが k より大きい場合は default)

        u: int
        v: int
        k: int
        default=-1: int
        """

        assert self.__after_seal_check(u,v)

        if k==0:
            return u

        # lca を求める.
        x=u; y=v
        dx=self.vertex_depth(x); dy=self.vertex_depth(y)
        if dx>dy:
            x,y=y,x
            dx,dy=dy,dx
        y=self.upper(y, dy-dx)

        if x==self.root or x==y:
            w=x
        else:
            bit=dx.bit_length()

            X=self.upper_list
            for t in range(bit-1,-1,-1):
                px=X[t][x]; py=X[t][y]
                if px!=py:
                    x=px; y=py
            w=self.parent[x]

        dist_uw=self.vertex_depth(u)-self.vertex_depth(w)
        dist_wv=self.vertex_depth(v)-self.vertex_depth(w)

        if dist_uw+dist_wv<k:
            return default
        elif k<=dist_uw:
            return self.upper(u, k)
        else:
            return self.upper(v, (dist_uw+dist_wv)-k)

    def is_leaf(self,v):
        """ 頂点 v は葉? """

        return not bool(self.children[v])

    def distance(self, u, v, faster=True):
        """ 2頂点 u, v 間の距離を求める. """

        assert self.__after_seal_check(u,v)

        dep=self.vertex_depth

        if faster:
            return dep(u)+dep(v)-2*dep(self.lowest_common_ancestor(u,v))
        else:
            return dep(u)+dep(v)-2*dep(self.lowest_common_ancestor_greedy(u,v))

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
        if hasattr(self, "preorder_number"):
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

    def dfs_yielder(self, order=None):
        """ DFS における頂点の出入りを yield する.

        以下のような関数を (仮想的に) 実行する.

        def dfs(v):
            yield (v,1) #頂点 v に入る
            for w in self.children[v]:
                dfs(w) #頂点 v を出る.
            yield (v,-1)

        order (1変数関数): for w in self.children[v] の順番を指定する (昇順) (※ 無い場合は任意, 破壊的)
        """
        assert self.__after_seal_check()

        #最初
        yield (self.root, 1)

        v=self.root

        ch=self.children
        pa=self.parent

        R=[-1]*self.index+[len(ch[x]) for x in range(self.index,self.index+self.N)]
        S=[0]*(self.index+self.N)

        if order!=None:
            for w in range(self.index, self.index+self.N):
                ch[w].sort(key=order)

        while True:
            if R[v]==S[v]:  #もし, 進めないならば
                yield (v,-1) #頂点vを出る
                if v==self.root:
                    break
                else:
                    v=pa[v]
            else:   #進める
                w=v
                v=ch[v][S[v]]
                S[w]+=1
                yield (v, 1)

    def top_down(self):
        """ 木の根から yield する. """

        assert self.__after_seal_check()
        if not hasattr(self, "tower"):
            self.depth_search(False)

        for layer in self.tower:
            yield from layer

    def bottom_up(self):
        """ 木の葉から yield する. """

        assert self.__after_seal_check()
        if not hasattr(self, "tower"):
            self.depth_search(False)

        for layer in self.tower[::-1]:
            yield from layer

    def tree_dp_from_leaf(self,merge,unit,f,g,Mode=False):
        """ 葉から木 DP 行う.

        [input]
        merge: 可換モノイドを成す2項演算 M x M -> M
        unit: M の単位元
        f: X x V x V → M: f(x,v,w): v が親, w が子
        g: M x V → X: g(x,v)
        Mode: False → 根の値のみ, True → 全ての値

        [補足]
        頂点 v の子が x,y,z,..., w のとき, 更新式は * を merge として
            dp[v]=g(f(dp[x],v,x)*f(dp[y],v,y)*f(dp[z],v,z)*...*f(dp[w],v,w), v)
        になる.
        """
        assert self.__after_seal_check()

        data=[unit]*(self.index+self.N)
        ch=self.children

        for x in self.bottom_up():
            for y in ch[x]:
                data[x]=merge(data[x], f(data[y], x, y))
            data[x]=g(data[x], x)

        if Mode:
            return data
        else:
            return data[self.root]

    def tree_dp_from_root(self, f, alpha):
        """ 根から木 DP を行う.

        [input]
        alpha: 初期値
        f: X x V x V → X: f(x,v,w): v が親, w が子

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

    def rerooting(self, merge, unit, f, g):
        """ 全方位木 DP を行う.

        [input]
        merge: 可換モノイドを成す2項演算 M x M -> M
        unit: M の単位元
        f: X x V x V → M: f(x,v,w): v が親, w が子
        g: M x V → X: g(x,v)

        ※ tree_dp_from_leaf と同じ形式

        [補足]
        頂点 v の子が x,y,z,..., w のとき, 更新式は * を merge として
            dp[v]=g(f(dp[x],v,x)*f(dp[y],v,y)*f(dp[z],v,z)*...*f(dp[w],v,w), v)
        になる.
        """
        assert self.__after_seal_check()

        upper=[unit]*(self.index+self.N)
        lower=[unit]*(self.index+self.N)

        ch=self.children
        pa=self.parent

        #DFSパート
        lower=self.tree_dp_from_leaf(merge, unit, f, g, True)

        #BFSパート
        for v in self.top_down():
            cc=ch[v]

            #累積マージ
            deg=len(cc)

            Left=[unit]; x=unit
            for c in cc:
                x=merge(x, f(lower[c], v, c))
                Left.append(x)

            Right=[unit]; y=unit
            for c in cc[::-1]:
                y=merge(y, f(lower[c], v, c))
                Right.append(y)
            Right=Right[::-1]

            for i in range(deg):
                c=cc[i]

                a=merge(Left[i], Right[i+1])

                if v!=self.root:
                    b=merge(a, f(upper[v], v, pa[v]))
                else:
                    b=a

                upper[c]=g(b, v)

        A=[unit]*(self.index+self.N)
        for v in range(self.index,self.index+self.N):
            if v!=self.root:
                a=f(upper[v], v, pa[v])
            else:
                a=unit

            for c in ch[v]:
                a=merge(a, f(lower[c], v, c))
            A[v]=g(a, v)
        return A

    def euler_tour_vertex(self, order=None):
        """ オイラーツアー (vertex) に関する計算を行う.

        order: 頂点の順番を指定する (破壊的)
        """

        assert self.__after_seal_check()
        if hasattr(self,"euler_vertex"):
            return

        #最初
        X=[-1]*(2*self.N-1) #X: Euler Tour (vertex) のリスト

        v=self.root

        ch=self.children
        if order!=None:
            for i in range(self.index,self.index+self.N):
                ch[i].sort(key=order)

        pa=self.parent

        R=[-1]*self.index+[len(ch[x]) for x in range(self.index,self.index+self.N)]
        S=[0]*(self.index+self.N)

        for t in  range(2*self.N-1):
            X[t]=v
            if R[v]==S[v]:
                v=pa[v]
            else:   #進める
                w=v
                v=ch[v][S[v]]
                S[w]+=1

        self.euler_vertex=X
        self.in_time=[-1]*(self.index+self.N)
        self.out_time=[-1]*(self.index+self.N)
        for t in range(2*self.N-1):
            v=X[t]
            if self.in_time[v]==-1:
                self.in_time[v]=self.out_time[v]=t
            else:
                self.out_time[v]=t

    def euler_tour_edge(self):
        """ オイラーツアー (edge) に関する計算を行う.

        (u, v, k): u から v へ向かう (k=+1 のときは葉へ進む向き, k=-1 のときは根へ進む向き)
        """

        assert self.__after_seal_check()
        if hasattr(self,"euler_edge"):
            return

        if not hasattr(self, "euler_vertex"):
            self.euler_tour_vertex()

        self.euler_edge=[0]*(2*(self.N-1))
        euler=self.euler_vertex
        pa=self.parent
        for t in range(2*(self.N-1)):
            u=euler[t]; v=euler[t+1]
            k=1 if u==pa[v] else -1
            self.euler_edge[t]=(u,v,k)

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

    def generated_subtree(self,S):
        """ S を含む最小の部分木の頂点を求める. """
        assert self.__after_seal_check(*S)

        if not hasattr(self, "in_time"):
            self.euler_tour_vertex()

        S=sorted(set(S),key=lambda i:self.in_time[i])
        K=len(S)

        T=set()
        for i in range(K-1):
            for a in self.path(S[i],S[i+1]):
                T.add(a)
        return sorted(T)

    def generated_subtree_size(self,S):
        """ S を含む最小の部分木のサイズを求める. """
        assert self.__after_seal_check(*S)

        if not hasattr(self, "in_time"):
            self.euler_tour_vertex()

        S=sorted(set(S),key=lambda i:self.in_time[i])
        K=len(S)

        X=0
        for i in range(K-1):
            X+=self.distance(S[i],S[i+1])
        return (X+self.distance(S[-1],S[0]))//2

#=================================================
def Making_Tree_from_Adjacent_List(N, A, root, index=0):
    """ 隣接リストから木を作る."""

    from collections import deque

    T=Tree(N, index)
    T.root_set(root)

    S=[False]*(N+index); S[root]=True
    Q=deque([root])
    while Q:
        v=Q.popleft()
        for w in A[v]:
            if not S[w]:
                S[w]=True
                T.parent_set(w,v)
                Q.append(w)

    T.seal()
    return T

def Making_Tree_from_Edges(N, E, root, index=0):
    """ 辺のリストから木を作る.

    N: 頂点数
    E: 辺のリスト E=[(u[0],v[0]), ..., (u[N-2], v[N-2]) ]
    root: 根
    """

    from collections import deque

    A=[[] for _ in range(N+index)]
    for u,v in E:
        A[u].append(v)
        A[v].append(u)

    T=Tree(N, index)
    T.root_set(root)

    S=[False]*(N+index); S[root]=True
    Q=deque([root])
    while Q:
        v=Q.popleft()
        for w in A[v]:
            if not S[w]:
                S[w]=True
                T.parent_set(w,v)
                Q.append(w)

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

def Breath_First_Search_Tree(N, A, root, index=0):
    from collections import deque

    T=Tree(N, index)
    T.root_set(root)

    S=[False]*(N+index); S[root]=True
    Q=deque([root])
    while Q:
        v=Q.popleft()
        for w in A[v]:
            if not S[w]:
                S[w]=True
                T.parent_set(w,v)
                Q.append(w)

    T.seal()
    return T

def Depth_First_Search_Tree(N, A, root, index=0):
    from collections import deque

    T=Tree(N,index); T.root_set(root)

    X=[False]*(N+index); X[root]=True
    R=[0]*(N+index)

    S=deque([root])
    while S:
        v=S.pop()
        X[v]=True

        while R[v]<len(A[v]):
            w=A[v][R[v]]
            R[v]+=1

            if not X[w]:
                S.append(v)
                S.append(w)
                T.child_set(v,w)
                continue
    T.seal()
    return T
