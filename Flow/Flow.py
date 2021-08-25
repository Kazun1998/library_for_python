#Thansk for  aaaaaaaaaa2230
#URL:https://atcoder.jp/contests/practice2/submissions/17017319
import sys
from collections import deque
class MaxFlow:
    class Edge:
        def __init__(self,target,cap,base,direct):
            self.target = target
            self.cap = cap
            self.flow=0
            self.base=base
            self.direct=direct
            self.rev = None

        def __str__(self):
            if self.direct==1:
                return "[S](target:{}, flow/cap:{}/{})".format(self.target,self.flow,self.base)
            else:
                return "[T](source:{}, flow/cap:{}/{})".format(self.target,self.flow,self.base)

        __repr__=__str__

    def __init__(self,N):
        """ N 頂点からなる Flow 場を生成する.
        """

        self.N = N
        self.graph = [[] for _ in range(N)]
        self.old_flow=0

    def add_edge(self,u,v, cap):
        """ 容量が cap である有向辺 u→v を加える.

        u,v: 頂点
        cap: 容量
        """
        graph = self.graph
        edge = self.Edge(v,cap,cap,1)
        edge2 = self.Edge(u,0,cap,-1)
        edge.rev = edge2
        edge2.rev = edge
        graph[u].append(edge)
        graph[v].append(edge2)

    def __bfs(self, s, t):
        level = self.level = [self.N]*self.N
        q = deque([s])
        level[s] = 0
        while q:
            now = q.popleft()
            lw = level[now]+1
            for e in self.graph[now]:
                if e.cap and level[e.target]> lw:
                    level[e.target] = lw
                    if e.target == t:
                        return True
                    q.append(e.target)
        return False

    def __dfs(self, s, t, up):
        graph = self.graph
        it = self.it
        level = self.level

        st = deque([t])
        while st:
            v = st[-1]
            if v == s:
                st.pop()
                flow = up
                for w in st:
                    e = graph[w][it[w]].rev
                    flow = min(flow, e.cap)
                for w in st:
                    e = graph[w][it[w]]
                    e.cap += flow
                    e.flow-=flow
                    e.rev.cap -= flow
                    e.rev.flow+=flow
                return flow
            lv = level[v]-1
            while it[v] < len(graph[v]):
                e = graph[v][it[v]]
                re = e.rev
                if re.cap == 0 or lv != level[e.target]:
                    it[v] += 1
                    continue
                st.append(e.target)
                break
            if it[v] == len(graph[v]):
                st.pop()
                level[v] = self.N

        return 0

    def max_flow(self,source,target,flow_limit=float("inf")):
        """ source から target に流す最大流の大きさを出力する.

        source, target: 頂点
        flow_limit: "追加で流す" 最大流の上限
        """

        Flow=0
        while Flow < flow_limit and self.__bfs(source,target):
            self.it=[0]*self.N
            while Flow<flow_limit:
                F=self.__dfs(source,target,flow_limit-Flow)
                if F==0:break
                Flow+=F
        self.old_flow+=Flow
        return self.old_flow

    def flow(self):
        """ 現在の flow の状況を求める.

        [Output]
        辞書 D が返る. D[u][v] で 有効辺 u→v に流れる量を表す.
        """

        X=[{} for _ in range(self.N)]
        for i in range(self.N):
            x=X[i]
            for e in self.graph[i]:
                if e.direct==-1: continue
                if e.target not in x: x[e.target]=0
                x[e.target]+=e.flow
        return X

    def min_cut(self,s):
        """ sにおける最小カットを求める.

        [Input]
        s: sorce (s が 0 側になる)

        [Output]
        0 or 1 のリストで, 0同士と1同士で分ける.
        """
        visited = [1]*self.N
        q = deque([s]); visited[s]=0
        while q:
            v = q.pop()
            for e in self.graph[v]:
                if e.cap and visited[e.target]==1:
                    visited[e.target]=0
                    q.append(e.target)
        return visited
