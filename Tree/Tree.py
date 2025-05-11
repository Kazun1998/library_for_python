from typing import TypeVar, Generator, Callable

X = TypeVar('X')
M = TypeVar('M')
class Tree:
    __slots__=("__N", "__index", "parent", "__mutable",
            "__root", "children", "__depth", "__tower", "upper_list", "__des_count", "preorder_number",
            "euler_vertex", "euler_edge", "in_time", "out_time", "lca_dst",
            "hld_hedge")

    @classmethod
    def make_tree_from_adjacent_list(cls, N: int, adj: list[list[int]], root: int, index: int = 0) -> "Tree":
        T = Tree(N, index)
        T.root_set(root)

        seen = [False] * (N + index)
        seen[root] = True

        stack = [root]

        while stack:
            x = stack.pop()

            for y in adj[x]:
                if seen[y]:
                    continue

                T.parent_set(y, x)
                stack.append(y)
                seen[y] = True

        T.seal()
        return T

    @classmethod
    def make_tree_from_edges(cls, N: int, edges: list[tuple[int, int]], root: int, index: int = 0) -> "Tree":
        adj = [[] for _ in range(index + N)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return cls.make_tree_from_adjacent_list(N, adj, root, index)

    # Property
    @property
    def N(self):
        return self.__N

    @property
    def index(self):
        return self.__index

    @property
    def root(self):
        return self.__root

    @property
    def mutable(self):
        return self.__mutable

    @property
    def depth(self):
        return self.__depth

    @property
    def tower(self):
        return self.__tower

    @property
    def des_count(self):
        return self.__des_count

    def __init__(self, N: int, index: int = 0):
        """ N 頂点 (index, index + 1, index + 2, ..., index + N - 1) を持つ木を生成する.

        Args:
            N (int): 頂点数
            index (int, optional): 最初の頂点番号. Defaults to 0.
        """

        self.__N = N
        self.__index = index
        self.parent = [-1] * (N + index)
        self.__mutable = True

    def vertex_exist(self, x: int) -> bool:
        """ 頂点 x が存在するかどうかを判定する. """

        return self.index <= x < self.index + self.N

    def __after_seal_check(self, *vertexes: int) -> bool:
        """ 木が確定していて, vertexes の頂点が存在するかどうかをチェックする. """

        if self.mutable:
            return False

        for v in vertexes:
            if not self.vertex_exist(v):
                return False
        return True

    #設定パート
    def root_set(self, root: int) -> None:
        """ 頂点 root を根に設定する.

        Args:
            root (int): 根にする頂点
        """

        assert self.vertex_exist(root)
        assert self.mutable

        self.__root = root

    def parent_set(self, x: int, y: int) -> None:
        """ 頂点 x の親を頂点 y に設定する.

        Args:
            x (int): 子
            y (int): 親
        """

        assert self.vertex_exist(x)
        assert self.vertex_exist(y)
        assert self.mutable

        self.parent[x] = y

    def child_set(self, x: int, y: int) -> None:
        """ 頂点 x の子の一つに頂点 y を設定する.

        Args:
            x (int): 親
            y (int): 子
        """

        assert self.vertex_exist(x)
        assert self.vertex_exist(y)
        assert self.mutable

        self.parent[y] = x

    def seal(self):
        """ 木の情報を確定させる (これ以降, 情報の変更は禁止)."""

        assert self.mutable
        assert hasattr(self, "root")

        children = [[] for _ in range(self.index + self.N)]
        parent = self.parent
        for v in range(self.index, self.index + self.N):
            if v == self.root:
                continue

            assert self.vertex_exist(parent[v])
            children[parent[v]].append(v)

        self.__mutable = False
        self.children = children
        self.__build_up()

    # 木を build up する.
    def __build_up(self):
        children = self.children
        depth = [-1] * (self.index+self.N)
        tower = [[] for _ in range(self.N)]

        stack = [self.root]
        depth[self.root] = 0
        tower[0] = [self.root]

        while stack:
            x = stack.pop()
            for y in children[x]:
                depth[y] = depth[x] + 1
                tower[depth[y]].append(y)
                stack.append(y)

        des_count = [0] * self.index + [1] * self.N
        for layer in reversed(tower):
            for x in layer:
                for y in self.children[x]:
                    des_count[x] += des_count[y]

        self.__depth = depth
        self.__tower = tower
        self.__des_count = des_count

    def vertex_depth(self, x):
        """ 頂点 x の深さを求める."""

        assert self.__after_seal_check(x)

        return self.depth[x]

    def __upper_list(self):
        assert self.__after_seal_check()

        if hasattr(self, "upper_list"):
            return

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

    def upper(self, x: int, k: int, over: bool = True) -> int:
        """ 頂点 x から見て k 個親の頂点を求める.

        Args:
            x (int): 元となる頂点
            k (int): 遡る世代
            over (bool, optional): (頂点 x の深さ) < k のときに True ならば根を返し, False ならばエラーを吐く. Defaults to True.

        Raises:
            ValueError: (頂点 x の深さ) < k かつ over = False のときにエラーを吐く.

        Returns:
            int: 頂点 x から見て k 個親の頂点
        """

        assert self.__after_seal_check(x)
        assert 0 <= k

        if not hasattr(self, "upper_list"):
            self.__upper_list()

        if self.vertex_depth(x) < k:
            if over:
                return self.root
            else:
                raise ValueError

        i=0
        while k:
            if k & 1:
                x = self.upper_list[i][x]
            k >>= 1
            i += 1
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
        dep=self.depth

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

    def degree(self, v: int) -> int:
        """ 頂点 v の次数を求める.

        Args:
            v (int): 頂点

        Returns:
            int: 次数
        """

        assert self.__after_seal_check(v)
        if v == self.root:
            return len(self.children[v])
        else:
            return len(self.children[v]) + 1

    def diameter(self) -> int:
        """ 木の直径を求める.

        Returns:
            int: 直径
        """

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

    def is_parent(self, u: int, v: int) -> bool:
        """ 頂点 u は頂点 v の親か?

        Args:
            u (int): 元となる頂点
            v (int): 親かどうかを判定する頂点

        Returns:
            bool: 親 ?
        """

        assert self.__after_seal_check(u, v)
        return (v != self.root) and (u == self.parent[v])

    def is_children(self, u: int, v: int) -> bool:
        """ 頂点 u は頂点 v の子か?

        Args:
            u (int): 元となる頂点
            v (int): 子かどうかを判定する頂点

        Returns:
            bool: 子 ?
        """

        assert self.__after_seal_check(u, v)
        return self.is_parent(v, u)

    def is_brother(self, u: int, v: int) -> bool:
        """ 頂点 u と頂点 v は兄弟か?

        Args:
            u (int): 頂点 1
            v (int): 頂点 2

        Returns:
            bool: 兄弟 ?
        """

        assert self.__after_seal_check(u,v)
        return (u != self.root) and (v != self.root) and (self.parent[u] == self.parent[v])

    def is_ancestor(self, u: int, v: int) -> bool:
        """ 頂点 u は頂点 v の先祖か?

        Args:
            u (int): 元となる頂点
            v (int): 先祖かどうかを判定する頂点

        Returns:
            bool: 先祖 ?
        """

        assert self.__after_seal_check(u,v)

        if (d := self.vertex_depth(v) - self.vertex_depth(u)) < 0:
            return False

        return u == self.upper(v,d)

    def is_descendant(self, u: int, v: int) -> bool:
        """ 頂点 u は頂点 v の子孫か?

        Args:
            u (int): 元となる頂点
            v (int): 子孫かどうかを判定する頂点

        Returns:
            bool: 子孫 ?
        """

        assert self.__after_seal_check(u, v)
        return self.is_ancestor(v, u)

    def direction(self, u: int, v: int) -> int:
        """ 頂点 u から頂点 v へのパス (u != v) に対して, 頂点 u の次に通る頂点

        Args:
            u (int): 始点
            v (int): 終点

        Returns:
            int: 頂点 u の次に通る頂点
        """

        assert self.__after_seal_check(u,v)
        assert u != v

        if self.is_ancestor(u, v):
            du = self.vertex_depth(u)
            dv = self.vertex_depth(v)
            return self.upper(v, dv - (du + 1))
        else:
            return self.parent[u]

    def jump(self, u: int, v: int, k: int, default = None) -> int:
        """ 頂点 u から頂点 v へ向かうパスにおいて k 番目 (0-indexed) に通る頂点 (パスの長さが k より大きい場合は default)

        Args:
            u (int): 始点
            v (int): 終点
            k (int): ジャンプの大きさ
            default (Any, optional): パスの長さが k より大きい場合の返り値. Defaults to None.

        Returns:
            int: 頂点 u から頂点 v へ向かうパスにおいて k 番目 に通る頂点
        """

        assert self.__after_seal_check(u,v)

        if k == 0:
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

    def is_leaf(self, v: int) -> bool:
        """ 頂点 v は葉?

        Args:
            v (int): 葉かどうかを判断する頂点

        Returns:
            bool: 葉 ?
        """

        return not bool(self.children[v])

    def distance(self, u, v, faster=True):
        """ 2頂点 u, v 間の距離を求める. """

        assert self.__after_seal_check(u,v)

        dep=self.vertex_depth

        if faster:
            return dep(u)+dep(v)-2*dep(self.lowest_common_ancestor(u,v))
        else:
            return dep(u)+dep(v)-2*dep(self.lowest_common_ancestor_greedy(u,v))


    def descendant_count(self, v: int) -> int:
        """ 頂点 v の子孫の数を求める.

        Args:
            v (int): 頂点

        Returns:
            int: 子孫の数
        """

        assert self.__after_seal_check(v)
        self.__descendant_count()
        return self.des_count[v]


    def subtree_size(self, v: int) -> int:
        """ 頂点 v を根とした部分根付き木のサイズを求める.

        Args:
            v (int): 頂点

        Returns:
            int: 部分根付き木のサイズ
        """

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

    def top_down(self) -> Generator[int, None, None]:
        """ 頂点を根から生成するジェネレーターを生成する.

        Yields:
            Generator[int, None, None]: 根からのジェネレータ
        """

        assert self.__after_seal_check()

        for layer in self.tower:
            yield from layer

    def bottom_up(self) -> Generator[int, None, None]:
        """ 頂点を葉から生成するジェネレーターを生成する.

        Yields:
            Generator[int, None, None]: 葉からのジェネレータ
        """

        assert self.__after_seal_check()
        for layer in self.tower[::-1]:
            yield from layer

    def tree_dp_from_leaf(self, merge: Callable[[M, M], M], unit: M, f: Callable[[X, int, int], M], g: Callable[[M, int], X]) -> list[X]:
        """ 葉からの木 DP を行う.

        [補足]
        頂点 v の子が x,y,z,..., w のとき, 更新式は * を merge として
            dp[v] = g(f(dp[x],v,x) * f(dp[y],v,y) * f(dp[z],v,z) * ... * f(dp[w],v,w), v)
        になる.

        Args:
            merge (Callable[[M, M], M]): 結果のマージ方法
            unit (M): モノイド M の単位元
            f (Callable[[X, int, int], M]): f: X x V x V → M: f(x,v,w): v が親, w が子
            g (Callable[[M, int], X]): M x V → X: g(x,v)

        Returns:
            list[X]: 各 v in V に対して, v を根とする部分木に関する結果
        """
        assert self.__after_seal_check()

        data = [unit] * (self.index + self.N)
        ch = self.children

        for x in self.bottom_up():
            for y in ch[x]:
                data[x] = merge(data[x], f(data[y], x, y))
            data[x] = g(data[x], x)

        return data

    def tree_dp_from_root(self, f: Callable[[X, int, int], X], alpha: X) -> list[X]:
        """ 根からの木 DP を行う.

        更新式は,
            dp[v] = alpha (v が根のとき), f(dp[v], parent[v], v) (v が根ではないとき)

        Args:
            f (Callable[[X, int, int], X]): v が根でないときの f(dp[v], parent[v], v).
            alpha (X): 初期値. つまり, 根の値

        Returns:
            list[X]: 木 DP の結果
        """

        assert self.__after_seal_check()

        data = [None] * (self.index + self.N)
        children = self.children

        data[self.root] = alpha
        for x in self.top_down():
            for y in children[x]:
                data[y] = f(data[x], x, y)

        return data

    def rerooting(self, merge, unit, f, g, h):
        """ 全方位木 DP を行う.

        [input]
        merge: 可換モノイドを成す2項演算 M x M -> M
        unit: M の単位元
        f: X x V x V → M: f(x,v,w): v が親, w が子
        g: M x V → X: g(x,v)

        ※ tree_dp_from_leaf と同じ形式

        [補足]
        頂点 v の子が x,y,z,..., w のとき, 更新式は + を merge として
            dp[v] = g(f(dp[x],v,x) + f(dp[y],v,y) + f(dp[z],v,z) + ... + f(dp[w],v,w), v) (v が根ではないとき)
                    h(f(dp[x],v,x) + f(dp[y],v,y) + f(dp[z],v,z) + ... + f(dp[w],v,w), v) (v が根のとき)
        になる.
        """
        assert self.__after_seal_check()

        children = self.children
        parent = self.parent

        #DFSパート
        lower = self.tree_dp_from_leaf(merge, unit, f, g)

        #BFSパート
        upper = [unit] * (self.index + self.N)
        for v in self.top_down():
            children_v = children[v]

            #累積マージ
            deg = len(children_v)

            left = [unit]; x = unit
            for c in children_v:
                x=merge(x, f(lower[c], v, c))
                left.append(x)

            right = [unit]; y = unit
            for c in children_v[::-1]:
                y = merge(y, f(lower[c], v, c))
                right.append(y)
            right = right[::-1]

            for i in range(deg):
                c = children_v[i]

                a = merge(left[i], right[i+1])
                b = a if self.root else merge(a, f(upper[v], v, parent[v]))
                upper[c] = g(b, v)

        result = [unit] * (self.index + self.N)
        for v in range(self.index, self.index + self.N):
            a = unit if v == self.root else f(upper[v], v, parent[v])

            for c in children[v]:
                a = merge(a, f(lower[c], v, c))

            result[v] = h(a, v)

        return result

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

        self.euler_vertex = X
        self.in_time = [-1] * (self.index + self.N)
        self.out_time = [-1] * (self.index + self.N)

        self.in_time[self.root] = 0
        self.out_time[self.root] = 2 * self.N - 1

        for t in range(1, 2 * self.N - 1):
            if self.is_parent(X[t - 1], X[t]):
                self.in_time[X[t]] = t
            else:
                self.out_time[X[t - 1]] = t

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

    def generated_subtree(self, S: list[int]) -> list[int]:
        """ S から生成する部分木を求める.

        Args:
            S (list[int]): 頂点集合の部分集合

        Returns:
            list[int]: 生成される部分木の頂点集合
        """

        assert self.__after_seal_check(*S)

        if not hasattr(self, "in_time"):
            self.euler_tour_vertex()

        S = sorted(set(S), key = lambda v: self.in_time[v])
        K = len(S)

        W = set()
        for i in range(K-1):
            W |= set(self.path(S[i], S[i+1]))
        return sorted(W)

    def generated_subtree_size(self, S: list[int]) -> int:
        """ S から生成する部分木のサイズ (辺の数) を求める.

        Args:
            S (list[int]): 頂点集合の部分集合

        Returns:
            int: 生成される部分木の頂点集合
        """

        assert self.__after_seal_check(*S)

        if not hasattr(self, "in_time"):
            self.euler_tour_vertex()

        S = sorted(set(S), key=lambda i: self.in_time[i])
        K = len(S)

        dist_sum = sum(self.distance(S[i], S[i + 1]) for i in range(K - 1))
        return (dist_sum + self.distance(S[-1], S[0])) // 2

    def subtree_hash(self, primes: list[int] = None, seed : list[int] = None, compress: bool = False) -> list:
        if primes is None:
            primes = [10 ** 9 + 7, 10 ** 9 + 9]

        if seed is None:
            from random import randint
            r = (1 << 63) - 1
            seed = [randint(0, r) for _ in range(self.N)]

        def build(p: int):
            h = [1] * self.N
            height = [0] * self.N

            for x in self.bottom_up():
                # 高さ更新
                height[x] = max((height[y] + 1 for y in self.children[x]), default = 0)

                # hash 計算
                a = seed[height[x]]
                for y in self.children[x]:
                    h[x] = h[x] * (a + h[y]) % p

            return h

        if not compress:
            return list(zip(*[build(p) for p in primes]))

        primes_prod = [1] * len(primes)
        for i in range(len(primes_prod) - 1):
            primes_prod[i + 1] = primes_prod[i] * primes[i]

        def hash_compress(h):
            k = 0
            for i in range(len(primes)):
                k = k * primes_prod[i] + h[i]
            return k

        return [hash_compress(h) for h in zip(*[build(p) for p in primes])]

#==================================================
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

def Breath_First_Search_Tree(N: int, adjacency_list: list[int], root: int, offset: int = 0) -> Tree:
    """adjacency_list を隣接リストとする root を根とする N 頂点の DFS 木を求める.

    Args:
        N (int): 位数
        adjacency_list (list[int]): 隣接リスト
        root (int): 根
        offset (int, optional): 頂点番号のオフセット. Defaults to 0.

    Returns:
        Tree: DFS 木
    """

    from collections import deque

    T = Tree(N, offset)
    T.root_set(root)

    seen = [False] * (N + offset)
    seen[root] = True

    queue = deque([root])
    while queue:
        v = queue.popleft()
        for w in adjacency_list[v]:
            if seen[w]:
                continue

            seen[w] = True
            T.parent_set(w, v)
            queue.append(w)

    T.seal()
    return T

def Depth_First_Search_Tree(N: int, adjacency_list: list[int], root: int, offset: int = 0) -> Tree:
    """adjacency_list を隣接リストとする root を根とする N 頂点の DFS 木を求める.

    Args:
        N (int): 位数
        adjacency_list (list[int]): 隣接リスト
        root (int): 根
        offset (int, optional): 頂点番号のオフセット. Defaults to 0.

    Returns:
        Tree: DFS 木
    """
    T = Tree(N, offset)
    T.root_set(root)

    X = [False] * (N + offset)
    X[root] = True
    R = [0] * (N + offset)

    stack = [root]
    while stack:
        v = stack.pop()
        X[v] = True

        while R[v] < len(adjacency_list[v]):
            w = adjacency_list[v][R[v]]
            R[v] += 1

            if X[w]:
                continue

            stack.append(v)
            stack.append(w)
            T.child_set(v, w)

    T.seal()
    return T
