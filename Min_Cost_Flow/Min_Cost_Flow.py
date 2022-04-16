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

    def __init__(self, N=0):
        """ 頂点数 N の Min Cost Flow 場を生成する.

        N: int
        """
        self.arc=[[] for _ in range(N)]
        self.__arc_list=[]
        self.__is_DAG=None

    def add_vertex(self):
        self.arc.append([])
        return self.vertex_count()-1

    def add_vertices(self, k):
        n=self.vertex_count()
        self.arc.extend([[] for _ in range(k)])
        return list(range(n,n+k))

    def add_arc(self, v, w, cap, cost):
        """ 頂点  v から頂点 w へ容量 cap, 費用 cost の有向辺を加える (返り値: 加えた辺の番号).

        v: 始点
        w: 終点
        cap: 容量
        cost: 費用
        """

        m=len(self.__arc_list)
        a=self.Arc(v, w, cap, cap, cost, 1, m)
        b=self.Arc(w, v, 0, cap, -cost, -1, m)
        a.rev=b
        b.rev=a
        self.arc[v].append(a)
        self.arc[w].append(b)
        self.__arc_list.append(a)

        return m

    def get_arc(self, i, mode=0):
        """ i 番目の辺の情報を得る.

        """
        assert 0<=i<len(self.__arc_list)
        a=self.__arc_list[i]
        if mode:
            return a,a.rev
        else:
            return a

    def get_all_arcs(self):
        return [self.get_arc(i) for i in range(len(self.__arc_list))]

    def vertex_count(self):
        return len(self.arc)

    def arc_count(self):
        return len(self.__arc_list)

    def change_arc(self, i, new_cap, new_flow, new_cost):
        """ i 番目の辺の情報を変更する.

        """

        assert 0<=i<len(self.__arc_list)
        assert 0<=new_flow<=new_cap

        a=self.__arc_list[i]
        a.base=new_cap; a.cap=new_cap-new_flow
        a.rev.base=new_cap; a.rev.cap=new_flow

    def __potential_by_Dijkstra(self, s):
        """ s を基準とするポテンシャルを Dijkstra 法によって求める.

        s: int
        """

        inf=Min_Cost_Flow.inf
        N=self.vertex_count()
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
        N=self.vertex_count()

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
        N=self.vertex_count()
        in_deg=[0]*N
        for i in range(self.arc_count()):
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

    def flow(self, source, target, flow):
        """ 頂点 s から頂点 t へ新たに流量 f を流す際の最小費用を求める.

        source: 始点
        target: 終点
        flow: 流量
        """
        assert 0<=flow
        return self.slope(source, target, flow)[-1]

    def slope(self, source, target, flow=-1):
        """ 流量と最小コストの関係図折れ線を出力する.

        source: 始点
        target: 終点
        flow: 流量
        """

        assert 0<=source<self.vertex_count()
        assert 0<=target<self.vertex_count()
        assert source!=target


        N=self.vertex_count(); inf=Min_Cost_Flow.inf
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
                g.append(g[-1]+self.__pot[target])

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
            F=[[] for _ in range(self.vertex_count())]
            for i,a in enumerate(self.__arc_list):
                F[a.source].append((i,a.target,a.base-a.cap))
            return F

    def refresh(self):
        for a in self.__arc_list:
            a.cap=a.base
            a.rev.cap=0
