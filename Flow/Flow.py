#Thansk for aaaaaaaaaa2230
#URL: https://atcoder.jp/contests/practice2/submissions/17017372

from collections import deque
class MaxFlow:
    inf = float("inf")

    class Arc:
        def __init__(self, to, cap, base, direction):
            self.to = to
            self.cap = cap
            self.base = base
            self.rev = None
            self.direction=direction

        def __repr__(self):
            if self.direction==1:
                return "[Source] (To: {}) {} / {}".format(self.to, self.cap,self.base)
            else:
                return "[Target] (From: {}) {} / {}".format(self.to, self.cap,self.base)

    def __init__(self, N):
        """ N 頂点のフロー場を生成する.
        """

        self.N=N
        self.arc = [[] for _ in range(N)]

    def add_arc(self, v, w, cap):
        """ 容量 cap の有向辺 v → w を加える.
        """

        a= self.Arc(w,cap,cap,1)
        a2 = self.Arc(v,0,cap,-1)
        a.rev = a2
        a2.rev = a
        self.arc[v].append(a)
        self.arc[w].append(a2)

    def add_edge(self, v, w, cap):
        """ 容量 cap の無向辺 v → w を加える."""
        self.add_arc(v,w,cap)
        self.add_arc(w,v,cap)

    def __bfs(self, s, t):
        level = self.level = [self.N]*self.N
        q = deque([s])
        level[s] = 0
        while q:
            now = q.popleft()
            lw = level[now]+1
            for a in self.arc[now]:
                if a.cap and level[a.to]> lw:
                    level[a.to] = lw
                    if a.to == t:
                        return True
                    q.append(a.to)
        return False

    def __dfs(self, s, t, up):
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
                if ra.cap == 0 or lv != level[a.to]:
                    it[v] += 1
                    continue
                st.append(a.to)
                break
            if it[v] == len(arc[v]):
                st.pop()
                level[v] = self.N
        return 0

    def max_flow(self, source, target, flow_limit=inf):
        """ source から target に高々 flow_limit の水流を流すとき, "新たに流れる" 水流の大きさ"""

        flow = 0
        while flow < flow_limit and self.__bfs(source, target):
            self.it = [0]*self.N
            while flow < flow_limit:
                f = self.__dfs(source, target, flow_limit-flow)
                if f == 0:
                    break
                flow += f
        return flow

    def flow(self):
        """ 現在の フロー場に流れている各辺の流量を求める.

        """

        F=[{} for _ in range(self.N)]
        arc=self.arc
        for v in range(self.N):
            for a in arc[v]:
                if a.direction==1:
                    F[v][a.to]=a.base-a.cap
        return F

    def min_cut(self,s):
        """ s を 0 に含める最小カットを求める.
        """

        group = [1]*self.N
        Q = deque([s])
        while Q:
            v = Q.pop()
            group[v] = 0
            for a in self.arc[v]:
                if a.cap and group[a.to]:
                    Q.append(a.to)
        return group
