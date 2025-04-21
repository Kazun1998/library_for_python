#Thansk for aaaaaaaaaa2230
#URL: https://atcoder.jp/contests/practice2/submissions/17017372

from collections import deque
class Max_Flow:
    inf = float("inf")

    class Arc:
        def __init__(self, source, target, cap, base, direction, id):
            self.source=source
            self.target=target
            self.cap = cap
            self.base = base
            self.rev = None
            self.direction=direction
            self.id=id

        def __repr__(self):
            if self.direction==1:
                return "id: {}, {} -> {}, {} / {}".format(self.id, self.source, self.target, self.cap, self.base)
            else:
                return "id: {}, {} <- {}, {} / {}".format(self.id, self.target, self.source, self.cap, self.base)

    def __init__(self, N: int = 0):
        """ N 頂点の最大フローを用意する.

        Args:
            N (int, optional): 位数. Defaults to 0.
        """

        self.arc = [[] for _ in range(N)]
        self.__arc_list=[]

    @property
    def order(self) -> int:
        """ 位数

        Returns:
            int: 位数
        """
        return len(self.arc)

    @property
    def vertex_count(self) -> int:
        """ 頂点数

        Returns:
            int: 頂点数
        """
        return len(self.arc)

    @property
    def size(self) -> int:
        """ サイズ

        Returns:
            int: サイズ
        """
        return len(self.__arc_list)

    @property
    def arc_count(self):
        """ 弧の数

        Returns:
            int: 弧の数
        """
        return len(self.__arc_list)

    def add_vertex(self) -> int:
        """ 頂点を 1 個追加する.

        Returns:
            int: 追加した頂点の番号
        """

        self.arc.append([])
        return self.vertex_count - 1

    def add_vertices(self, k: int) -> int:
        """ 頂点を k 個追加する.

        Args:
            k (int): 追加する頂点の数

        Returns:
            int: 追加する k 個の頂点の番号からなるリスト
        """

        n = self.vertex_count
        self.arc.extend([[] for _ in range(k)])
        return list(range(n, n + k))

    def add_arc(self, v: int, w: int, cap: int) -> int:
        """ 容量 cap の弧 v → w を追加する.

        Args:
            v (int): 始点
            w (int): 終点
            cap (int): 容量

        Returns:
            int: 追加した弧の番号
        """


        m = self.size
        a=self.Arc(v,w,cap,cap,1,m)
        b=self.Arc(w,v,0,cap,-1,m)
        a.rev=b; b.rev=a
        self.arc[v].append(a)
        self.arc[w].append(b)
        self.__arc_list.append(a)

        return m

    def get_arc(self, i: int) -> Arc:
        """ i 番目の弧を得る.

        Args:
            i (int): 弧の番号

        Returns:
            Arc: 弧
        """

        assert 0 <= i < self.size
        self.__arc_list[i]

    def get_all_arcs(self):
        return [self.get_arc(i) for i in range(self.size)]

    def change_arc(self, i, new_cap, new_flow):
        """ i 番目の辺の情報を変更する.

        """

        assert 0<= i < self.size
        assert 0<=new_flow<=new_cap

        a=self.__arc_list[i]
        a.base=new_cap; a.cap=new_cap-new_flow
        a.rev.base=new_cap; a.rev.cap=new_flow

    def add_edge(self, v, w, cap):
        """ 容量 cap の無向辺 v → w を加える."""
        self.add_arc(v,w,cap)
        self.add_arc(w,v,cap)

    def __bfs(self, s: int, t: int) -> bool:
        level=self.level=[-1]*self.vertex_count
        Q=deque([s])
        level[s]=0
        while Q:
            v=Q.popleft()
            next_level=level[v]+1
            for a in self.arc[v]:
                if a.cap and level[a.target]==-1:
                    level[a.target]=next_level
                    if a.target==t:
                        return True
                    Q.append(a.target)
        return False

    def __dfs(self, s: int, t: int, up: int) -> int:
        arc = self.arc
        it = self.it
        level = self.level

        st = deque([t])
        while st:
            v = st[-1]
            if v == s:
                st.pop()
                flow = up
                for w in st:
                    a = arc[w][it[w]].rev
                    flow = min(flow, a.cap)
                for w in st:
                    a = arc[w][it[w]]
                    a.cap += flow
                    a.rev.cap -= flow
                return flow
            lv = level[v]-1
            while it[v] < len(arc[v]):
                a = arc[v][it[v]]
                ra = a.rev
                if ra.cap == 0 or lv != level[a.target]:
                    it[v] += 1
                    continue
                st.append(a.target)
                break
            if it[v] == len(arc[v]):
                st.pop()
                level[v]=-1
        return 0

    def max_flow(self, source: int, target: int, flow_limit: int = inf) -> int:
        """ source から target へ flow_limit を上限として流せるだけ流したときの "追加で発生する" 流量を求める.

        Args:
            source (int): 始点
            target (int): 終点
            flow_limit (int, optional): 流量の上限. Defaults to inf.

        Returns:
            int: "追加で発生する" 流量
        """

        flow = 0
        while flow < flow_limit and self.__bfs(source, target):
            self.it = [0]*self.vertex_count
            while flow < flow_limit:
                f = self.__dfs(source, target, flow_limit-flow)
                if f == 0:
                    break
                flow += f
        return flow

    def get_flow(self, mode=0):
        if mode==0:
            return [a.base-a.cap for a in self.__arc_list]
        else:
            F=[[] for _ in range(self.vertex_count)]
            for i,a in enumerate(self.__arc_list):
                F[a.source].append((i, a.target, a.base-a.cap))
            return F

    def min_cut(self, s: int) -> list[int]:
        """ s を 0 側に含める最小カットを求める.

        Args:
            s (int): 頂点番号

        Returns:
            list[int]: 0, 1 からなる長さが位数のリスト. 最小カットは 0 側と 1 側に分かれる. 頂点 s は必ず 0 側になる.
        """

        group = [1] * self.vertex_count
        Q = deque([s])
        while Q:
            v = Q.pop()
            group[v] = 0
            for arc in self.arc[v]:
                if arc.cap and group[arc.target]:
                    Q.append(arc.target)
        return group

    def refresh(self):
        for a in self.__arc_list:
            a.cap=a.base
            a.rev.cap=0
