#Thansk for aaaaaaaaaa2230
#URL: https://atcoder.jp/contests/practice2/submissions/17017372

from collections import deque

class Arc:
    def __init__(self, source: int, target: int, cap: int, base: int, direction: int, id: int):
        self.source = source
        self.target = target
        self.cap = cap
        self.base = base
        self.rev: Arc = None
        self.direction = direction # 1 が順, -1 が逆順
        self.id = id

    def __repr__(self):
        return f"{self.__class__.__name__}(source={self.source}, target={self.target}, cap={self.cap}, base={self.base}, direction={self.direction}, id={self.id})"

class Max_Flow:
    inf = float("inf")

    def __init__(self, N: int = 0):
        """ N 頂点の最大フローを用意する.

        Args:
            N (int, optional): 位数. Defaults to 0.
        """

        self.arc: list[list[Arc]] = [[] for _ in range(N)]
        self.__arc_list: list[Arc] =[]

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
        arc = Arc(v, w, cap, cap, 1, m)
        arc_rev = Arc(w, v, 0, cap, -1, m)
        arc.rev = arc_rev
        arc_rev.rev = arc
        self.arc[v].append(arc)
        self.arc[w].append(arc_rev)
        self.__arc_list.append(arc)

        return m

    def get_arc(self, i: int) -> Arc:
        """ i 番目の弧を得る.

        Args:
            i (int): 弧の番号

        Returns:
            Arc: 弧
        """

        assert 0 <= i < self.size
        return self.__arc_list[i]

    def get_all_arcs(self) -> list[Arc]:
        return [self.get_arc(i) for i in range(self.size)]

    def change_arc(self, i, new_cap, new_flow):
        """ i 番目の辺の情報を変更する.

        """

        assert 0 <= i < self.size
        assert 0 <= new_flow<=new_cap

        a=self.__arc_list[i]
        a.base=new_cap; a.cap=new_cap-new_flow
        a.rev.base=new_cap; a.rev.cap=new_flow

    def add_edge(self, v, w, cap):
        """ 容量 cap の無向辺 v → w を加える."""
        self.add_arc(v,w,cap)
        self.add_arc(w,v,cap)

    def __bfs(self, s: int, t: int) -> bool:
        level = self.level = [-1] * self.vertex_count
        Q = deque([s])
        level[s] = 0
        while Q:
            v = Q.popleft()
            next_level = level[v] + 1
            for arc in self.arc[v]:
                if not(arc.cap and level[arc.target] == -1):
                    continue

                level[arc.target] = next_level
                if arc.target == t:
                    return True

                Q.append(arc.target)

        return False

    def __dfs(self, s: int, t: int, up: int) -> int:
        arc_to = self.arc
        it = self.it
        level = self.level

        st = deque([t])
        while st:
            v = st[-1]
            if v == s:
                break

            lv = level[v]-1
            while it[v] < len(arc_to[v]):
                arc_rev = arc_to[v][it[v]]
                arc = arc_rev.rev
                if arc.cap == 0 or lv != level[arc.source]:
                    it[v] += 1
                    continue
                st.append(arc.source)
                break

            if it[v] == len(arc_to[v]):
                st.pop()
                level[v] = -1
        else:
            return 0

        st.pop()
        flow = up
        for w in st:
            arc = arc_to[w][it[w]].rev
            flow = min(flow, arc.cap)

        for w in st:
            arc_rev = arc_to[w][it[w]]
            arc_rev.cap += flow
            arc_rev.rev.cap -= flow

        return flow

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
            self.it = [0] * self.vertex_count
            while flow < flow_limit:
                f = self.__dfs(source, target, flow_limit - flow)
                if f == 0:
                    break
                flow += f
        return flow

    def get_flow(self) -> list[list[tuple[int, int, int]]]:
        F = [[] for _ in range(self.vertex_count)]
        for arc in self.__arc_list:
            F[arc.source].append((arc.id, arc.target, arc.base - arc.cap))
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
            a.cap = a.base
            a.rev.cap = 0
