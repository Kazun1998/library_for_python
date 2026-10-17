from heapq import heappush, heappop
class Min_Cost_Flow:
    #最小費用流問題

    inf=float("inf")

    class Arc:
        __slots__=("source", "target", "cap", "base", "rev", "cost", "direction", "id")

        def __init__(self, source, target, cap, base, cost, direction, id):
            self.source=source
            self.target=target
            self.cap=cap
            self.base=base
            self.cost=cost
            self.rev=None
            self.direction=direction
            self.id=id

        def __repr__(self):
            if self.direction==1:
                return "id: {}, {} -> {}, {} / {}, cost: {}".format(self.id, self.source, self.target, self.cap, self.base, self.cost)
            else:
                return "id: {}, {} <- {}, {} / {}, cost: {}".format(self.id, self.target, self.source, self.cap, self.base, self.cost)

    def __init__(self, N: int = 0, objective: int = 1):
        """ 頂点数 N の最小費用流の場を用意する.

        Args:
            N (int, optional): 頂点数. Defaults to 0.
            objective (int, optional): -1 にすると, 最大費用流になる. Defaults to 1.
        """

        self.arc: list[list] = [[] for _ in range(N)]
        self.__arc_list=[]
        self.__objective=objective
        self.__is_DAG=None

    def add_vertex(self) -> int:
        """ 頂点を 1 個追加する.

        Returns:
            int: 追加した頂点の番号
        """

        self.arc.append([])
        return self.vertex_count - 1

    def add_vertices(self, k: int) -> list[int]:
        """ 頂点を k 個追加する.

        Args:
            k (int): 追加する頂点の個数

        Returns:
            list[int]: 追加した頂点の番号からなるリスト
        """

        n = self.vertex_count
        self.arc.extend([[] for _ in range(k)])
        return list(range(n, n + k))

    @property
    def order(self) -> int:
        return len(self.arc)

    @property
    def vertex_count(self) -> int:
        return len(self.arc)

    @property
    def size(self) -> int:
        return len(self.__arc_list)

    @property
    def arc_count(self) -> int:
        return len(self.__arc_list)

    def add_arc(self, v: int, w: int, cap: int, cost: int) -> int:
        """ 頂点 v から頂点 w への伸びる容量 cap, 1 単位あたりの費用が cost の弧を貼る.

        Args:
            v (int): 始点
            w (int): 終点
            cap (int): 容量
            cost (int): 1 単位当たりの費用

        Returns:
            int: 追加した弧の番号
        """

        m = self.size
        a = self.Arc(v, w, cap, cap, self.__objective * cost, 1, m)
        b = self.Arc(w, v, 0, cap, -self.__objective * cost, -1, m)
        a.rev = b
        b.rev = a
        self.arc[v].append(a)
        self.arc[w].append(b)
        self.__arc_list.append(a)

        return m

    def get_arc(self, i: int) -> Arc:
        """ i 番目の辺を得る.

        Args:
            i (int): 辺の番号

        Returns:
            Arc: i 番目の辺
        """

        assert 0 <= i < self.size
        return self.__arc_list[i]

    def get_all_arcs(self):
        return [self.get_arc(i) for i in range(self.size)]

    def change_arc(self, i, new_cap, new_flow, new_cost):
        """ i 番目の辺の情報を変更する.

        """

        assert 0<=i<self.size
        assert 0<=new_flow<=new_cap

        a=self.__arc_list[i]
        a.base=new_cap; a.cap=new_cap-new_flow
        a.rev.base=new_cap; a.rev.cap=new_flow

    def __potential_by_Dijkstra(self, s):
        """ s を基準とするポテンシャルを Dijkstra 法によって求める.

        s: int
        """

        inf=Min_Cost_Flow.inf
        N=self.vertex_count
        self.__pre_v=[-1]*N
        self.__pre_e=[None]*N
        self.__dist=[inf]*N; self.__dist[s]=0

        Q=[(0,s)]
        while Q:
            d,v=heappop(Q)

            if d>self.__dist[v]:
                continue

            for a in self.arc[v]:
                w=a.target
                if a.cap>0 and self.__dist[w]>d+self.__pot[v]-self.__pot[w]+a.cost:
                    self.__dist[w]=d+self.__pot[v]-self.__pot[w]+a.cost
                    self.__pre_v[w]=v
                    self.__pre_e[w]=a
                    heappush(Q, (self.__dist[w],w))
        return

    def __potential_for_DAG(self, s):
        """ DAG 上における s を基準とするポテンシャルを求める.

        s: int
        """

        inf=Min_Cost_Flow.inf
        N=self.vertex_count

        self.__pre_v=[-1]*N
        self.__pre_e=[None]*N
        self.__dist=[inf]*N; self.__dist[s]=0

        for v in self.__top_sort:
            for a in self.arc[v]:
                w=a.target
                if a.direction==1 and self.__dist[w]>self.__dist[v]+a.cost:
                    self.__dist[w]=self.__dist[v]+a.cost
                    self.__pre_v[w]=v
                    self.__pre_e[w]=a

    def __topological_sort(self):
        N=self.vertex_count
        in_deg=[0]*N
        for i in range(self.arc_count):
            in_deg[self.__arc_list[i].target]+=1

        Q=[v for v in range(N) if in_deg[v]==0]
        T=[]
        while Q:
            v=Q.pop()
            T.append(v)

            for a in self.arc[v]:
                w=a.target
                if a.direction==1:
                    in_deg[w]-=1
                    if in_deg[w]==0:
                        Q.append(w)

        if len(T)==N:
            self.__is_DAG=True
            self.__top_sort=T
        else:
            self.__is_DAG=False
            self.__top_sort=None

    def __potential(self, s):
        """ s を基準とするポテンシャルを求める.

        s: int
        """

        if self.__is_DAG==None:
            self.__topological_sort()

        if self.__is_DAG:
            self.__potential_for_DAG(s)
            self.__is_DAG=False
        else:
            self.__potential_by_Dijkstra(s)
        return

    def flow(self, source: int, target: int, flow: int) -> int:
        """ 頂点 source から頂点 target へ流用 flow だけ流したときの最小費用を求める

        Args:
            source (int): 始点
            target (int): 終点
            flow (int): 流量

        Returns:
            int: 最小費用
        """

        assert 0<=flow
        return self.slope(source, target, flow)[-1]

    def slope(self, source: int, target: int, flow: int = -1) -> list[int]:
        """ f = 0, 1, 2, ..., flow に対して, 頂点 source から頂点 target へ流用 f だけ流したときの最小費用を求める.

        Args:
            source (int): 始点
            target (int): 終点
            flow (int, optional): 調べる流用の最大値. -1 にすると, 流せるだけ流す.. Defaults to -1.

        Returns:
            list[int]: 最大流を F として, f = 0, 1, ..., min(F, flow) に対して, 第 f 要素は流用 f だけ流したときの最小費用.
        """

        assert 0<=source<self.vertex_count
        assert 0<=target<self.vertex_count
        assert source!=target


        N=self.vertex_count
        inf=Min_Cost_Flow.inf
        self.__pot=[0]*N

        g=[0]

        if flow<0:
            flow=Min_Cost_Flow.inf

        while flow:
            self.__potential(source)

            if self.__dist[target]==inf:
                break

            for v in range(N):
                self.__pot[v]+=self.__dist[v]

            push=flow; u=target
            while u!=source:
                push=min(push, self.__pre_e[u].cap)
                u=self.__pre_v[u]

            flow-=push

            for _ in range(push):
                g.append(g[-1]+self.__objective*self.__pot[target])

            u=target
            while u!=source:
                a=self.__pre_e[u]
                a.cap-=push; a.rev.cap+=push
                u=self.__pre_v[u]
        return g

    def get_flow(self, mode=0):
        if mode==0:
            return [a.base-a.cap for a in self.__arc_list]
        else:
            F=[[] for _ in range(self.vertex_count)]
            for i,a in enumerate(self.__arc_list):
                F[a.source].append((i,a.target,a.base-a.cap))
            return F

    def refresh(self):
        for a in self.__arc_list:
            a.cap=a.base
            a.rev.cap=0

class Max_Gain_Flow(Min_Cost_Flow):
    def __init__(self, N=0):
        Min_Cost_Flow.__init__(self, N, -1)
